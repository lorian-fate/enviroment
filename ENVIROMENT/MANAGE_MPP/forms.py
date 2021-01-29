from django import forms
from django.contrib.auth.forms import  UserCreationForm
from .models import UserOver


class User_PerfilesForm(UserCreationForm):
    class Meta:
        model = UserOver
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]
    


    