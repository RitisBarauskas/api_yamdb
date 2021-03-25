from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.core.validators import MinValueValidator, MaxValueValidator

from .settings import *


class User(AbstractUser):
    first_name = models.CharField(
        FIRST_NAME_VERBOSE_NAME,
        max_length=NAME_MAX_LENGTH,
        blank=True
    )
    last_name = models.CharField(
        LAST_NAME_VERBOSE_NAME,
        max_length=NAME_MAX_LENGTH,
        blank=True
    )
    username = models.CharField(
        USERNAME_VERBOSE_NAME,
        unique=True,
        max_length=NAME_MAX_LENGTH
    )
    bio = models.TextField(
        BIO_VERBOSE_NAME,
        max_length=BIO_MAX_LENGTH,
        blank=True
    )
    email = models.EmailField(
        EMAIL_VERBOSE_NAME,
        max_length=EMAIL_MAX_LENGTH,
        unique=True
    )
    role = models.CharField(
        ROLE_VERBOSE_NAME,
        max_length=ROLE_MAX_LENGTH,
        blank=True
    )


class Category(models.Model):
    name = models.CharField(
        CATEGORY_NAME_VERBOSE_NAME,
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True
    )
    slug = models.SlugField(
        max_length=SLUG_MAX_LENGTH,
        unique=True
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        GENRE_VERBOSE_NAME,
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True
    )
    slug = models.SlugField(
        max_length=SLUG_MAX_LENGTH,
        unique=True
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        TILE_VERBOSE_NAME,
        max_length=TITLE_NAME_MAX_LENGTH,
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name=TITLE_RELATED_NAME
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=DO_NOTHING,
        related_name=TITLE_RELATED_NAME
    )
    description = models.TextField(
        DESCRIPTION_VERBOSE_NAME,
        blank=True,
        null=True
    )
    year = models.DecimalField(
        YEAR_VERBOSE_NAME,
        max_digits=YEAR_MAX_DIGITS,
        decimal_places=YEAR_DECIMAL_PLACES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(
        REVIEW_VERBOSE_NAME,
        max_length=TEXT_MAX_LENGTH
    )
    author = models.ForeignKey(
        User,
        verbose_name=AUTHOR_VERBOSE_NAME,
        on_delete=models.CASCADE,
        related_name=REVIEW_RELATED_NAME
    )
    score = models.PositiveSmallIntegerField(
        SCORE_VERBOSE_NAME,
        default=SCORE_DEFAULT,
        validators=[
            MinValueValidator(SCORE_MIN_VALUE),
            MaxValueValidator(SCORE_MAX_VALUE)
        ],
        blank=False,
        null=False
    )
    title = models.ForeignKey(
        Title,
        verbose_name=TILE_VERBOSE_NAME,
        on_delete=models.CASCADE,
        related_name=REVIEW_RELATED_NAME,
    )
    pub_date = models.DateTimeField(
        PUB_DATE_VERBOSE_NAME,
        auto_now_add=True,
    )

    class Meta:
        unique_together = ('author', 'title')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(
        COMMENT_VERBOSE_NAME,
        max_length=TEXT_MAX_LENGTH
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name=COMMENT_RELATED_NAME,
        verbose_name=AUTHOR_VERBOSE_NAME
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name=COMMENT_RELATED_NAME,
        verbose_name=REVIEW_VERBOSE_NAME
    )
    pub_date = models.DateTimeField(
        PUB_DATE_VERBOSE_NAME,
        auto_now_add=True,
    )

    def __str__(self):
        return self.review
