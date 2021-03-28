from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import generate_confirmation_code
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import DO_NOTHING
from .settings import *


ROLE_VERBOSE_NAME = 'role'
EMAIL_VERBOSE_NAME = 'email'
BIO_VERBOSE_NAME = 'bio'
CONFIRMATION_CODE_VERBOSE_NAME = 'confirmation code'
USERNAME_VERBOSE_NAME = 'username'
FIRST_NAME_VERBOSE_NAME = 'first name'
LAST_NAME_VERBOSE_NAME = 'last name'

ROLE_MAX_LENGTH = 30
EMAIL_MAX_LENGTH = 30
BIO_MAX_LENGTH = 300
CONFIRMATION_CODE_MAX_LENGTH = 30
USERNAME_MAX_LENGTH = 30
FIRST_NAME_MAX_LENGTH = 30
LAST_NAME_MAX_LENGTH = 30


USER_ROLES = [
    ('admin', 'Администратор'),
    ('moderator', 'Модератор'),
    ('user', 'Пользователь'),
]


class User(AbstractUser):
    username = models.CharField(
        USERNAME_VERBOSE_NAME,
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        null=True,
        blank=True
    )
    first_name = models.CharField(
        FIRST_NAME_VERBOSE_NAME,
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        LAST_NAME_VERBOSE_NAME,
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True
    )
    role = models.CharField(
        ROLE_VERBOSE_NAME,
        choices=USER_ROLES,
        max_length=ROLE_MAX_LENGTH,
        default='user',
        null=True,
        blank=True)  
    email = models.EmailField(
        EMAIL_VERBOSE_NAME,
        max_length=EMAIL_MAX_LENGTH,
        unique=True
    )
    bio = models.TextField(
        BIO_VERBOSE_NAME,
        max_length=BIO_MAX_LENGTH,
        blank=True
    )    
    confirmation_code = models.CharField(
        CONFIRMATION_CODE_VERBOSE_NAME,
        max_length=CONFIRMATION_CODE_MAX_LENGTH,
        null=True,
        default=generate_confirmation_code(CONFIRMATION_CODE_MAX_LENGTH)
    )

    REQUIRED_FIELDS = ['role', 'email']

    @property
    def is_admin(self):
        return self.is_staff or self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'
    
    def __str__(self):
        return str(self.username)
   

SCORE_VALIDATORS = (MinValueValidator(SCORE_MIN_VALUE), MaxValueValidator(SCORE_MAX_VALUE))


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Id {self.pk}: {self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Id {self.pk}: {self.name}'


class Title(models.Model):
    name = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre, related_name='titles')
    category = models.ForeignKey(Category, null=True, on_delete=DO_NOTHING,
                                 related_name='titles')
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Id {self.pk}: {self.name}, {self.year}'


class Review(models.Model):
    """Reviews of works
    Review is linked to a specific piece of work.
    """

    text = models.TextField(REVIEW_VERBOSE_NAME, max_length=TEXT_MAX_LENGTH)
    author = models.ForeignKey(User, verbose_name=AUTHOR_VERBOSE_NAME, on_delete=models.CASCADE, related_name=REVIEW_RELATED_NAME)
    title = models.ForeignKey(Title, verbose_name=TILE_VERBOSE_NAME, on_delete=models.CASCADE, related_name=REVIEW_RELATED_NAME)
    pub_date = models.DateTimeField(PUB_DATE_VERBOSE_NAME, auto_now_add=True)
    score = models.PositiveSmallIntegerField(SCORE_VERBOSE_NAME, default=SCORE_DEFAULT, validators=SCORE_VALIDATORS,
                                      blank=False, null=False)

    def __str__(self):
        return self.title
