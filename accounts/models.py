from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    class UserTypes(models.TextChoices):
        AUTHOR = 'AU', _('Author')
        STAFF = 'ST', _('Staff')

    user_type = models.CharField(max_length=3, choices=UserTypes.choices, default=UserTypes.AUTHOR)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

