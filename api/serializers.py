from rest_framework import serializers

<<<<<<< HEAD
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role',)
        model = User
=======

class CategoriesSerializer(serializers.ModelSerializer):
    pass


class GenresSerializer(serializers.ModelSerializer):
    pass


class TotlesSerializer(serializers.ModelSerializer):
    pass
>>>>>>> 9b775e7 (модельки)
