from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.managers import UserManager


class User(AbstractUser):
	email = models.EmailField(
		max_length=255,
		blank=False,
		unique=True,
		verbose_name=_("Email"),
	)
	
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []
	
	objects = UserManager()
	
	def save(self, *args, **kwargs):
		self.email = self.email.lower()
		super(User, self).save(*args, **kwargs)
	
	class Meta:
		db_table = 'auth_user'
		verbose_name = "Пользователь"
		verbose_name_plural = "Пользователи"