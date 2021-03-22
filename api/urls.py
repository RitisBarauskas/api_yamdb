from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router_v1 = DefaultRouter()
router_v1.register('v1/users', UserViewSet, basename='user')

urlpatterns = [path('', include(router_v1.urls)),]