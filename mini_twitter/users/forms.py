from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, UserProfile


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat your password'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class ChangeUserInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ['birthday', 'first_name', 'last_name', 'email']
        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата народження'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Прізвище'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Імя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),

        }


class ChangeUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Біографія'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Аватар'}),
        }
