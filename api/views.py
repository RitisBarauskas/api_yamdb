from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .permissions import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.filters import TitleFilter
from .permissions import *

from .models import Category, Genre, Title
from .serializers import (CategoriesSerializer, GenresSerializer,
                          TitleSerializerGet, TitlesSerializer)
from .utils import ObjectViewSetMixin


class CategoriesViewSet(ObjectViewSetMixin):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminOrReadOnly, )
    pagination_class = PageNumberPagination
    lookup_field = 'slug'
    filter_backends = (SearchFilter, )
    search_fields = ('name', )


class GenresViewSet(ObjectViewSetMixin):
    serializer_class = GenresSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsAdminOrReadOnly, )
    pagination_class = PageNumberPagination
    lookup_field = 'slug'
    filter_backends = (SearchFilter, )
    search_fields = ('name', )


class TitlesViewSet(ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score')).order_by('id')
    filter_backends = (DjangoFilterBackend, SearchFilter)
    permission_classes = ((IsAuthenticatedOrReadOnly, IsAdminOrReadOnly))
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleSerializerGet
        else:
            return TitlesSerializer