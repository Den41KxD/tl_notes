# swagger_urls.py
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path

schema_view = get_schema_view(
	openapi.Info(
		title="API Docs",
		default_version='v1',
		description="API documentation",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="contact@example.com"),
		license=openapi.License(name="BSD License"),
	),
	public=True,
	permission_classes=[permissions.IsAuthenticated,],
)

urlpatterns = [
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]