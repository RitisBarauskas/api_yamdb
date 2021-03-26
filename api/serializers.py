from rest_framework.serializers import ModelSerializer, CharField, SlugRelatedField, ValidationError, IntegerField

from .models import Category, Comment, Genre, Review, Title, User
from .settings import *


class UserSerializer(ModelSerializer):
    """User serialiser."""

    role = CharField(default=USER_ROLE)

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role', 'confirmation_code')
        model = User
        extra_kwargs = {
            'confirmation_code': {'write_only': True},
            'username': {'required': True},
            'email': {'required': True}
        }


class ReviewSerializer(ModelSerializer):
    """Review serialiser."""

    author = SlugRelatedField(AUTHOR_SLUG_FIELD, read_only=True, many=False)

    class Meta:
        read_only_fields = ('id', 'title', 'pub_date')
        fields = '__all__'
        model = Review

    def validate(self, attrs):
        is_exist = Review.objects.filter(author=self.context['request'].user,
                                         title=self.context['view'].kwargs.get('title_id')).exists()
        if is_exist and self.context['request'].method == 'POST':
            raise ValidationError()
        return attrs


class CommentSerializer(ModelSerializer):
    """Comment serialiser."""

    author = SlugRelatedField(AUTHOR_SLUG_FIELD, read_only=True, many=False)

    class Meta:
        read_only_fields = ('id', 'review', 'pub_date')
        fields = '__all__'
        model = Comment


class CategorySerializer(ModelSerializer):
    """Category serialiser."""

    class Meta:
        fields = ('name', 'slug')
        model = Category
        lookup_field = 'slug'


class GenreSerializer(ModelSerializer):
    """Genre serialiser."""

    class Meta:
        fields = ('name', 'slug')
        model = Genre
        lookup_field = 'slug'


class TitleListSerializer(ModelSerializer):
    """Serialiser for the output of a list of works."""

    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitleCreateSerializer(ModelSerializer):
    """Serialiser for the creation of works."""

    category = SlugRelatedField(SLUG_FIELD, queryset=Category.objects.all())
    genre = SlugRelatedField(SLUG_FIELD, queryset=Genre.objects.all(), many=True)

    class Meta:
        fields = '__all__'
        model = Title
