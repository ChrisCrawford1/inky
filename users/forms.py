from django import forms
from django.contrib.auth.forms import UsernameField


class UserLoginForm(forms.Form):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control col-md-4 m-auto mb-md-3",
                "placeholder": "John Doe",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control col-md-4 m-auto mb-md-3",
                "placeholder": "**********",
            }
        )
    )
