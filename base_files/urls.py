from django.contrib.auth.decorators import login_required
from django.urls import path

from base_files.views import DashboardView, Login, Register, Logout

urlpatterns = [
    path('', login_required(DashboardView.as_view(), login_url='/login/'), name='dashboard'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
]