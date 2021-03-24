<<<<<<< HEAD
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


=======
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_NULL


User = get_user_model()


class Categories(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True)


class Genres(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True)


class Titles(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    genre = models.ManyToManyField(Genres, related_name='titles')
    category = models.ForeignKey(Categories, null=True, on_delete=DO_NOTHING,
                                 related_name='titles')
    description = models.TextField(blank=True, null=True)
    year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
>>>>>>> 9b775e7 (модельки)
