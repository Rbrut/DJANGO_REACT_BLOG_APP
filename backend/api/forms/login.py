from django import forms

class LoginForm(forms.Form):
    field = [
        'username',
        'password',
    ]