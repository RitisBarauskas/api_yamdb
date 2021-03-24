<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from api.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
=======
from django.shortcuts import render
from .utils import ObjectViwSetMixin


class CategoriesViewSet(ObjectViwSetMixin):

    pass


class GenresViewSet(ObjectViwSetMixin):

    pass


class TitlesViewSet(ObjectViwSetMixin):

    pass
>>>>>>> 9b775e7 (модельки)
