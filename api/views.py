
from api.utils import generate_confirmation_code
from rest_framework.views import APIView
from .models import CONFIRMATION_CODE_MAX_LENGTH, User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAdmin, IsModerator, IsSuperuser, IsAdminOrReadOnly
from rest_framework.response import Response
from django.core.mail import send_mail



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
    pass


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsSuperuser)
    # permission_classes = (IsAuthenticatedOrReadOnly,)
