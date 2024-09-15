from rest_framework.routers import DefaultRouter

from note.viewsets import NoteViewSet

router = DefaultRouter()

router.register('note', NoteViewSet, basename='page-contacts')

urlpatterns = []

urlpatterns += router.urls

