from celery.bin.control import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils import timezone
from django.db.models import Q

from note.models import Note
from note.serializers import NoteSerializer
from rest_framework.status import HTTP_201_CREATED


class NoteViewSet(ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer
	permission_classes = (IsAuthenticated,)
	
	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)
	
	@action(detail=False, methods=['post'])
	def continue_task(self, request):
		# Текущая дата
		today = timezone.now().date()
		# Получаем последнюю заметку, созданную текущим пользователем сегодня
		last_note = Note.objects.filter(
			Q(created_by=request.user) &
			Q(created_at__date=today)
		).order_by('-created_at').first()
		
		if last_note:
			last_note: Note
			last_note.created_at = timezone.now()
			last_note.save()
			return Response(status=HTTP_201_CREATED, data=self.get_serializer(last_note).data)
		else:
			return Response({"detail": "No notes found."}, status=404)