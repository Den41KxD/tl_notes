from django.views.generic import TemplateView, ListView
from rest_framework.response import Response
from rest_framework.views import APIView

from note.models import Note, DailyReport
from note.statistic_generator import generate_ai_report


class UserNoteView(ListView):
	model = Note
	template_name = "pages/notes.html"
	queryset = Note.objects.all()
	
	def get_queryset(self):
		return super().get_queryset().filter(created_by=self.request.user).order_by('-created_at')
	

class ReportsView(ListView):
	model = DailyReport
	template_name = "pages/reports.html"
	queryset = DailyReport.objects.all()
	
	def get_queryset(self):
		return super().get_queryset().filter(user=self.request.user).order_by('created_at')

	
class GenerateReport(APIView):
	def post(self, request):
		start_datetime = request.data.get('start_datetime')
		end_datetime = request.data.get('end_datetime')
		if not start_datetime or not end_datetime:
			return Response(status=400, data={'error': 'Invalid request data'})
		generate_ai_report.delay(user_id=request.user.id, start_time=start_datetime, end_time=end_datetime)
		return Response(status=200)