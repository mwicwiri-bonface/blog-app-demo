from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    class UserTypes(models.TextChoices):
        AUTHOR = 'AU', _('Author')
        STAFF = 'ST', _('Staff')

    user_type = models.CharField(max_length=3, choices=UserTypes.choices, default=UserTypes.AUTHOR)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()
    phone_number = PhoneNumberField(blank=True)
    country = CountryField()
    image = models.ImageField(upload_to="profiles/%Y/%m/", default="profiles/default.png")
