from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.deletion import DO_NOTHING

from .settings import *

User = get_user_model()

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
    year = models.DecimalField(max_digits=4, decimal_places=0,
                               blank=True, null=True)

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
