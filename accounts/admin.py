from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ngettext

from accounts.forms import UserAdminChangeForm, RegistrationForm
from accounts.models import User, Profile

admin.site.site_header = "Suchana Blog Admin"
admin.site.site_title = "Suchana Blog Admin Portal"
admin.site.index_title = "Welcome to Suchana Blog Management System Portal"

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = RegistrationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('first_name', 'last_name', 'email', 'username', 'user_type')
    search_fields = ('first_name', 'last_name', 'email', 'username',)
    list_filter = ('is_active', 'user_type')

    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'username')}),
        ('Permissions', {'fields': ('user_type',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', 'user_type', 'password1', 'password2')}
         ),
    )
    ordering = ['email']
    filter_horizontal = ()

    @staticmethod
    def has_delete_permission(request, obj=None):
        return False

    @staticmethod
    def has_change_permission(request, obj=None):
        return True

    @staticmethod
    def has_add_permission(request, obj=None):
        return True


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    search_fields = ['user__username']
    list_display = ['user', 'phone_number', 'image', 'country']
    list_display_links = ['user', ]
    search_help_text = "Search by username"
    list_filter = ('updated', 'created')

    @staticmethod
    def has_change_permission(request, obj=None):
        return True
