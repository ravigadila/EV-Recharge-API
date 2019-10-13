import os
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordResetForm, AuthenticationForm

from .models import User


class RegisterForm(forms.ModelForm):
    """Registration form for new users
    """
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "confirm_password"]

    def clean_confirm_password(self):
        """Check for password and confirm_password matching
        """
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords doesn't match")
        return confirm_password


class LoginForm(AuthenticationForm):
    """Login Form with email and password
    """
    pass


class ProfileForm(forms.ModelForm):
    """User Profile edit form
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "date_of_birth"]


class PasswordResetEmailForm(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("Error: There is no user registered with the specified email address!")
        return email