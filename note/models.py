from django.db import models

from user.models import User


class Note(models.Model):
    text = models.TextField()
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notes')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    