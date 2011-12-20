from django import forms
from users.models import UserProfile
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):
    email = forms.EmailField(required=True, max_length=75)
    password = forms.CharField(required=True, min_length=6, max_length=30, widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            UserProfile.objects.get(user__email=email)
            raise ValidationError('Email Already Picked!')
        except UserProfile.DoesNotExist:
            return email

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, max_length=75)
    password = forms.CharField(required=True, min_length=6, max_length=30, widget=forms.PasswordInput())
