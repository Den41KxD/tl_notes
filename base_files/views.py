from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView

from base_files.forms import UserCreation


class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return '/'


class Register(CreateView):
    form_class = UserCreation
    template_name = 'register.html'
    success_url = '/'


class Logout(LogoutView):
    next_page = '/'
    login_url = 'login/'


class DashboardView(TemplateView):
    template_name = "dashboard.html"
