from django.contrib import admin

from note.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	list_display = ['text', 'created_by', 'is_read', 'created_at', 'task_id']
	list_filter = ('created_at', 'created_by')
