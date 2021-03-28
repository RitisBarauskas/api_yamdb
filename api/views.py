from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet

from api.filters import TitleFilter
from api.permissions import IsAdminOrReadOnly

from .models import Category, Genre, Title
from .serializers import (CategoriesSerializer, GenresSerializer,
                          TitleSerializerGet, TitlesSerializer)
from .utils import ObjectViewSetMixin


class CategoriesViewSet(ObjectViewSetMixin):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()
    permission_classes = (BasePermission, )
    pagination_class = PageNumberPagination
    lookup_field = 'slug'
    filter_backends = (SearchFilter, )
    search_fields = ('name', )


class GenresViewSet(ObjectViewSetMixin):
    serializer_class = GenresSerializer
    queryset = Genre.objects.all()
    permission_classes = (BasePermission, )
    pagination_class = PageNumberPagination
    lookup_field = 'slug'
    filter_backends = (SearchFilter, )
    search_fields = ('name', )


class TitlesViewSet(ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    filter_backends = (DjangoFilterBackend, SearchFilter)
    pagination_class = PageNumberPagination
    permission_classes = (BasePermission, )
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleSerializerGet
        else:
            return TitlesSerializer