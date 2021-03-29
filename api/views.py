from django.core.mail import send_mail
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (AllowAny, BasePermission,
                                        IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from api.filters import TitleFilter
from api.utils import generate_confirmation_code

from .models import CONFIRMATION_CODE_MAX_LENGTH, Category, Genre, Title, User
from .permissions import *
from .serializers import (CategoriesSerializer, GenresSerializer,
                          TitleSerializerGet, TitlesSerializer, UserSerializer)
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet


class ObjectViewSetMixin(ListModelMixin,
                         CreateModelMixin,
                         DestroyModelMixin,
                         GenericViewSet):
    pass


class CreateUser(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        email = request.data.get('email')
        user = User.objects.filter(email=email)
        if user.exists():
            confirmation_code = user[0].confirmation_code
        else:
            confirmation_code = generate_confirmation_code(CONFIRMATION_CODE_MAX_LENGTH)
            data = {
                'email': email,
                'confirmation_code': confirmation_code,
                'username': email
            }
            serializer = UserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        user.send_mail(subject='Register', message=confirmation_code, from_email='test@yamdb.com')
        return Response({'email': email})



class TakeToken(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get_token(user):
        return str(RefreshToken.for_user(user).access_token)

    def post(self, request):
        user = get_object_or_404(User, email=request.data.get('email'))
        if user.confirmation_code != request.data.get('confirmation_code'):
            return Response({'confirmation_code': 'Неверно указан код подтверждения'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'token': self.get_token(user)}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsSuperuser)
    lookup_field = 'username'

    @action(detail=False, methods=('get', 'patch'), permission_classes=(IsAuthenticated,))
    def me(self, request):
        if request.method == 'GET':
            return Response(self.get_serializer(request.user, many=False).data)
        else:
            serializer = self.get_serializer(instance=request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


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
    queryset = Title.objects.annotate(rating=Avg('reviews__score')).order_by('id')
    filter_backends = (DjangoFilterBackend, SearchFilter)
    permission_classes = ((BasePermission, ))
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleSerializerGet
        else:
            return TitlesSerializer
