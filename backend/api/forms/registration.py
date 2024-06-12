from django import forms
from api.models.user import User

class RegistrationForm(forms.ModelForm):
    model = User
    fields = [
        'username',
        'email',
        'password'
    ]