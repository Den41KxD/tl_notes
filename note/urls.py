from rest_framework.routers import DefaultRouter

from note.views import UserNoteView, ReportsView, GenerateReport
from note.viewsets import NoteViewSet

from django.contrib.auth.decorators import login_required
from django.urls import path

router = DefaultRouter()

router.register('note', NoteViewSet, basename='page-contacts')

urlpatterns = [
	path('notes', login_required(UserNoteView.as_view(), login_url='/login/'), name='user_notes'),
	path('reports', login_required(ReportsView.as_view(), login_url='/login/'), name='reports'),
	path('start_generate_report/', GenerateReport.as_view(), name='start_generate_report'),
	
]

urlpatterns += router.urls

