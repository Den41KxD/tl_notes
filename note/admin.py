from django.contrib import admin

from note.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	pass
