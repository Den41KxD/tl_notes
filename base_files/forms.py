from django.contrib.auth.forms import UserCreationForm

from user.models import User


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')