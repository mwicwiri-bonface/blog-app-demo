from django.forms import ModelForm

from blog.models import Category, Tag, Blog


class CategoryModelForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class TagModelForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class BlogModelForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'content', 'tags', 'category', 'image', 'keywords', 'short_description', 'description']
