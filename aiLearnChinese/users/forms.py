from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    LANGUAGE_LEVELS = (
        ('option 1', 'Beginner'),
        ('option 2', 'Intermediate'),
        ('option 3', 'Advanced')
    )
    email = forms.EmailField(required=True)
    language_level = forms.ChoiceField(choices=LANGUAGE_LEVELS)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'language_level']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
