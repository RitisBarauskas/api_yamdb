
from django.shortcuts import get_object_or_404
from api.utils import generate_confirmation_code
from rest_framework.views import APIView
from .models import CONFIRMATION_CODE_MAX_LENGTH, User
from .serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAdmin, IsModerator, IsSuperuser
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action



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
    
    @action(detail=False, methods=('get', 'patch'), url_path='me', permission_classes=(IsAuthenticated,))
    def get_or_update_self(self, request):
        if request.method == 'GET':
            return Response(self.get_serializer(request.user, many=False).data)
        else:
            serializer = self.get_serializer(instance=request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
