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
