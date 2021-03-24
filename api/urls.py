from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet


router = DefaultRouter()
router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitlesViewSet, basename='titles')
router.register('titles/<int:titles_id>', TitlesViewSet, basename='titles')
router.register('genres/<str:slug>', GenresViewSet, basename='genres')
router.register('categories/<str:slug>', CategoriesViewSet, basename='categories')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'), ]
