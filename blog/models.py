from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from core.utils import TimeStampModel

User: AbstractUser = get_user_model()


class Category(TimeStampModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Tag(TimeStampModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Blog(TimeStampModel):
    name = models.CharField(max_length=250, unique=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextUploadingField(config_name='default')
    image = models.ImageField(upload_to="images/%Y/%m", default="images/default.png")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    keywords = models.CharField(max_length=250, help_text="used for seo")
    description = models.TextField(help_text="used for seo")
    short_description = models.TextField(help_text="used for seo")

    def __str__(self):
        return self.name