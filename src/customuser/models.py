from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager,
    PermissionsMixin,
)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model that support using email"""
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    
    objects = UserManager()

    
