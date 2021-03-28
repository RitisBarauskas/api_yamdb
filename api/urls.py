from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CreateUser, TakeToken


router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/email/', CreateUser.as_view(), name='create_user' ),
    path('v1/auth/token/', TakeToken.as_view(), name='take_token' ),
]
