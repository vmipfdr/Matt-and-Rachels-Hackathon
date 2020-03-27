from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')