from django_filters import CharFilter, FilterSet

from .models import Title
from .settings import (TITLE_CATEGORY_FILTER_FIELD, TITLE_FILTER_FIELDS,
                       TITLE_GENRE_FILTER_FIELD, TITLE_NAME_FILTER_FIELD)


class TitleFilter(FilterSet):
    """Filter works by name, category, genre, year."""

    name = CharFilter(
        field_name=TITLE_NAME_FILTER_FIELD,
        lookup_expr='contains'
    )
    category = CharFilter(
        field_name=TITLE_CATEGORY_FILTER_FIELD,
        lookup_expr='exact'
    )
    genre = CharFilter(
        field_name=TITLE_GENRE_FILTER_FIELD,
        lookup_expr='exact'
    )

    class Meta:
        model = Title
        fields = TITLE_FILTER_FIELDS
