from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from api.models import User

from .serializers import UserSerializer
from .utils import ObjectViwSetMixin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoriesViewSet(ObjectViwSetMixin):

    pass


class GenresViewSet(ObjectViwSetMixin):

    pass


class TitlesViewSet(ObjectViwSetMixin):

    pass
