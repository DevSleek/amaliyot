from django import forms
from django.core import validators

from .models import UserModel


class UserCreateForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'message')



