from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog.forms import CategoryModelForm, TagModelForm, BlogModelForm
from blog.models import Category, Tag, Blog


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    form = CategoryModelForm
    add_form = CategoryModelForm
    search_fields = ['name']
    list_display = ['slug', 'name', 'created', 'updated']
    list_display_links = ['slug', ]
    search_help_text = "Search by name"
    list_filter = ('updated', 'created')

    @staticmethod
    def has_change_permission(request, obj=None):
        return True


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    form = TagModelForm
    add_form = TagModelForm
    search_fields = ['name']
    list_display = ['slug', 'name', 'created', 'updated']
    list_display_links = ['slug', ]
    search_help_text = "Search by name"
    list_filter = ('updated', 'created')

    @staticmethod
    def has_change_permission(request, obj=None):
        return True


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    form = BlogModelForm
    add_form = BlogModelForm
    search_fields = ['name']
    list_display = ['slug', 'name', 'category', 'created', 'updated']
    list_display_links = ['slug', ]
    search_help_text = "Search by name"
    list_filter = ('updated', 'created')

    @staticmethod
    def has_change_permission(request, obj=None):
        return True

