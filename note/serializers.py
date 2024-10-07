from rest_framework import serializers

from note.models import Note


class NoteSerializer(serializers.ModelSerializer):
	task_id = serializers.IntegerField(required=False, allow_null=True)
	created_at = serializers.DateTimeField(required=False)
	
	class Meta:
		model = Note
		fields = '__all__'
		read_only_fields = ('created_by',)