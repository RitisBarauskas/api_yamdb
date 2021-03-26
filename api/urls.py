from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
from .views import UserViewSet


router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='user')
# router_v1.register('auth/email', NewToken, basename='newtoken')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('verification/', include('verify_email.urls')),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]