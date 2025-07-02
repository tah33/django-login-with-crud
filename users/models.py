from django.contrib.auth.models import AbstractUser
from django.db import models

class AuthUser(AbstractUser):
    class Meta:
        db_table = 'auth_user'
    phone = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='users/images/', blank=True)