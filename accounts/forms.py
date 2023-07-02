from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField
)


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label=_("Username"),
        widget=forms.TextInput(
            attrs={
                'placeholder': "Username",
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        max_length=255, 
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Password",
                'class': 'form-control'
            }
        )
    )


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=255, 
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Password"
            }
        )
    )
    password2 = forms.CharField(
        max_length=255, 
        label=_("Confirm Password"),
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Confirm Password"
            }
        )
    )
    description = forms.CharField(
        max_length=255,
        label=_("Description"),
        widget=forms.Textarea(attrs={'placeholder': "Description"})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2','description')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })