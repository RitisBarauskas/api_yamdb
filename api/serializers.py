from rest_framework import serializers

from .models import Category, Genre, Title, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role', 'confirmation_code',)
        model = User
        extra_kwargs = {
            'confirmation_code': {'write_only': True},
            'username': {'required': True},
            'email': {'required': True}
        }


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitlesSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())
    genre = serializers.SlugRelatedField(slug_field='slug',
                                         queryset=Genre.objects.all(),
                                         many=True)
                        
    class Meta:
        model = Title
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleSerializerGet(serializers.ModelSerializer):
    category = CategoriesSerializer()
    genre = GenresSerializer(many=True)
    rating = serializers.ImageField()

    class Meta:
        model = Title
        fields = '__all__'
