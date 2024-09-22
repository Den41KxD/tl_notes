from datetime import datetime

import openai
from celery import shared_task
from django.conf import settings
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from note.models import Note, DailyReport
from user.models import User



class StatisticGenerator:
	def __init__(self, user: User):
		self.user = user
		
		
	def start_generate_report(self, start_time: datetime, end_time: datetime) -> dict:
		queryset = Note.objects.filter(created_by=self.user)
		if start_time and end_time :
			queryset=queryset.filter(
				created_at__range=(start_time, end_time)).order_by('created_at')
		formatted_notes = []
		preview_note = None
		for count, i in enumerate(queryset):
			if not count:
				note_text = f"Начало рабочего дня с  {i.text}"
				formatted_notes.append(note_text)
				preview_note = i
				continue
			note_text = f"[{preview_note.created_at.strftime('%H:%M')}-{i.created_at.strftime('%H:%M')}] {i.text}"
			preview_note = i
			
			if i.task_id:
				note_text += f" (Task link: {i.task_url()})"
			
			formatted_notes.append(note_text)
		daile_report, _  = DailyReport.objects.get_or_create(
			user=self.user,
			created_at= timezone.now().date(),
		)
		
		daile_report: DailyReport
		daile_report.text = self.generate_daily_report(formatted_notes)
		daile_report.in_progress = False
		daile_report.save()

	def generate_daily_report(self, notes: list) -> str:
		
		openai.api_key = settings.OPENAI_API_KEY
		
		notes_text = "\n".join(notes)
		messages = [
			{
				"role": "system",
				"content": "Generate a daily report based on the following notes. The report should be in Russian and in a list format with timelines. Merge similar notes into a single timeline entry. Each entry should be a new list item in an HTML string."
			},
			{
				"role": "user",
				"content": notes_text
			}
		]
		
		try:
			response = openai.ChatCompletion.create(
				model="gpt-4",
				messages=messages,
				max_tokens=1000
			)
			
			return response.choices[0].message['content'].strip()
		
		except Exception as e:
			# Handle any errors that occur during the API call
			return f"An error occurred while generating the report: {str(e)}"
	

@shared_task
def generate_ai_report(user_id: int, start_time: str, end_time: str):
	
	StatisticGenerator(User.objects.get(id=user_id)).start_generate_report(start_time=parse_datetime(start_time), end_time=parse_datetime(end_time))