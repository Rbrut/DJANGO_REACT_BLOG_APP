from django import forms
from api.models.post import Post

class PostForm(forms.ModelForm):
    model = Post
    field = [
        'title',
        'description',
        'body',
        'image',
    ]