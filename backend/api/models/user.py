from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    joined = models.DateField(auto_created=True, auto_now_add=True, verbose_name='joined on')

    REQUIRED_FIELDS = ['email']