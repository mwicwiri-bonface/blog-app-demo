from django.contrib.auth import get_user_model, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, ReadOnlyPasswordHashField
from django.forms import ModelForm, forms

from accounts.models import Profile

User = get_user_model()


class UserAuthenticationForm(AuthenticationForm):

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.upper()

    def clean(self):
        super().clean()
        if self.user_cache is None or self.user_cache.is_staff:
            logout(self.request)
            raise forms.ValidationError('Invalid username or password or both', code='invalid login')
        elif self.user_cache.is_archived:
            logout(self.request)
            raise forms.ValidationError('Sorry your account is archived', code='invalid login')


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'user_type', 'password1', 'password2']

    def clean_username(self):
        data = self.cleaned_data['username']
        return data.upper()


class UserAdminChangeForm(ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admins
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'is_active']

    def clean_username(self):
        data = self.cleaned_data['username']
        return data.upper()

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class ProfileModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone_number', 'image', 'country']
