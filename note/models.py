from django.utils import timezone

from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Note(models.Model):
    text = CKEditor5Field('Text', config_name='default')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, verbose_name=_("Created at"))
    task_id = models.CharField(max_length=100, verbose_name=_("Task ID"), blank=True, null=True)
    
    
    def task_url(self):
        return f'https://crm.alsodev.com/_module/task/view/task/{self.task_id}'
    
    def __str__(self):
        return self.text[:50]
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super().save(*args, **kwargs)
        
    
class DailyReport(models.Model):
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True, unique_for_date=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_reports')
    in_progress = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Отчет за день'
        verbose_name_plural = 'Отчеты'