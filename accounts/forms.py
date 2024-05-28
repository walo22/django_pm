from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django import forms


attrs = {'class': 'form-control'}


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args: Any, **kwargs):
        super(UserLoginForm, self).__init__( *args, **kwargs)


    username = forms.CharField(
        label= 'Username',
        widget=forms.TextInput(attrs=attrs)

    )
    username = forms.CharField(
        label= 'Password',
        widget=forms.PasswordInput(attrs=attrs)
        
    )