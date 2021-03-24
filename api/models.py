from django.db import models
from django.contrib.auth.models import AbstractUser
# from .manage import UserManager



class User(AbstractUser):
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    username = models.CharField('username', unique=True, max_length=30)
    bio = models.TextField('bio', max_length=500, blank=True)
    email = models.EmailField('email address', unique=True)
    role = models.CharField('role', max_length=30, blank=True)

    # objects = UserManager()
    
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # class Meta:
    #     verbose_name = 'user'
    #     verbose_name_plural = 'users'


