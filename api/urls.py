from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CreateUser, TakeToken, CategoriesViewSet, GenresViewSet, TitlesViewSet


router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='user')
router_v1.register('categories', CategoriesViewSet, basename='categories')
router_v1.register('genres', GenresViewSet, basename='genres')
router_v1.register('titles', TitlesViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/email/', CreateUser.as_view(), name='create_user' ),
    path('v1/auth/token/', TakeToken.as_view(), name='take_token' ),
]
