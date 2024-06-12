import uuid
from django.db import models
from api.models.user import User
from api.models.category import Category
from django_extensions.db.models import TitleSlugDescriptionModel


class Post(TitleSlugDescriptionModel, models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    image = models.ImageField(upload_to='post/', blank=True)
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    body = models.TextField()
    created = models.DateField(auto_created=True, auto_now_add=True)
    modified = models.DateField(auto_created=True, auto_now=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
