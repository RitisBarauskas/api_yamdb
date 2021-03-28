from django_filters import CharFilter, NumberFilter
from django_filters import rest_framework as filters

from .models import Title
from .settings import *


class TitleFilter(filters.FilterSet):
    name = CharFilter(field_name=TITLE_NAME_FILTER_FIELD, lookup_expr='contains')
    genre = CharFilter(field_name='genre__slug')
    category = CharFilter(field_name='category__slug')
    year = NumberFilter
    

    class Meta:
        model = Title
        fields = ['name', 'category', 'genre', 'year']
