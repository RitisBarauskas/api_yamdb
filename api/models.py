from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import generate_confirmation_code


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


class UserRole(models.Choices):
    user = 'user', 'Пользователь'
    moderator = 'moderator', 'Модератор'
    admin = 'admin', 'Администратор'


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
        max_length=ROLE_MAX_LENGTH,
        blank=True
    )
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
        return self.is_staff or self.role == UserRole.admin

    @property
    def is_moderator(self):
        return self.role == UserRole.moderator
    
    def __str__(self):
        return str(self.username)
    