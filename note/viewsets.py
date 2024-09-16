from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from note.models import Note
from note.serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer
	permission_classes = (IsAuthenticated,)
	
	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)