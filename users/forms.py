from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class UserRegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPES, required=True)
    email = forms.EmailField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'user_type')


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

