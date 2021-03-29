from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (CASCADE, CharField, DateTimeField, EmailField,
                              ForeignKey, IntegerField, ManyToManyField, Model,
                              PositiveSmallIntegerField, SlugField, TextField)
from django.db.models.deletion import DO_NOTHING

from .settings import (ADMIN_ROLE, AUTHOR_VERBOSE_NAME, BIO_MAX_LENGTH,
                       BIO_VERBOSE_NAME, CATEGORY_NAME_VERBOSE_NAME,
                       COMMENT_RELATED_NAME, COMMENT_VERBOSE_NAME,
                       CONFIRMATION_CODE_LEN, CONFIRMATION_CODE_VERBOSE_NAME,
                       DESCRIPTION_VERBOSE_NAME, EMAIL_MAX_LENGTH,
                       EMAIL_VERBOSE_NAME, GENRE_VERBOSE_NAME, MODERATOR_ROLE,
                       NAME_MAX_LENGTH, PUB_DATE_VERBOSE_NAME,
                       REVIEW_RELATED_NAME, REVIEW_VERBOSE_NAME,
                       ROLE_MAX_LENGTH, ROLE_VERBOSE_NAME, SCORE_DEFAULT,
                       SCORE_MAX_VALUE, SCORE_MIN_VALUE, SCORE_VERBOSE_NAME,
                       SLUG_MAX_LENGTH, TEXT_MAX_LENGTH, TITLE_NAME_MAX_LENGTH,
                       TITLE_RELATED_NAME, TITLE_VERBOSE_NAME,
                       YEAR_VERBOSE_NAME)
from .utils import generate_confirmation_code

SCORE_VALIDATORS = (
    MinValueValidator(SCORE_MIN_VALUE),
    MaxValueValidator(SCORE_MAX_VALUE)
)


class User(AbstractUser):
    """User augmented fields."""

    bio = TextField(
        BIO_VERBOSE_NAME,
        max_length=BIO_MAX_LENGTH,
        blank=True
    )
    role = CharField(
        ROLE_VERBOSE_NAME,
        max_length=ROLE_MAX_LENGTH,
        blank=True
    )
    email = EmailField(
        EMAIL_VERBOSE_NAME,
        max_length=EMAIL_MAX_LENGTH,
        unique=True
    )
    confirmation_code = CharField(
        CONFIRMATION_CODE_VERBOSE_NAME,
        max_length=CONFIRMATION_CODE_LEN,
        null=True,
        default=generate_confirmation_code(CONFIRMATION_CODE_LEN)
    )

    @property
    def is_admin(self):
        return self.is_staff or self.role == ADMIN_ROLE

    @property
    def is_moderator(self):
        return self.role == MODERATOR_ROLE


class Category(Model):
    """Types of works (Movies, Books, Music)."""

    name = CharField(
        CATEGORY_NAME_VERBOSE_NAME,
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True
    )
    slug = SlugField(
        max_length=SLUG_MAX_LENGTH,
        unique=True
    )

    def __str__(self):
        return self.name


class Genre(Model):
    """Genres of works

    One work can be linked to more than one genre.
    """

    name = CharField(
        GENRE_VERBOSE_NAME,
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True
    )
    slug = SlugField(
        max_length=SLUG_MAX_LENGTH,
        unique=True
    )

    def __str__(self):
        return self.name


class Title(Model):
    """Works for which reviews are written."""

    name = CharField(
        TITLE_VERBOSE_NAME,
        max_length=TITLE_NAME_MAX_LENGTH,
        blank=True,
        null=True
    )
    genre = ManyToManyField(
        Genre,
        related_name=TITLE_RELATED_NAME
    )
    category = ForeignKey(
        Category,
        related_name=TITLE_RELATED_NAME,
        null=True,
        on_delete=DO_NOTHING
    )
    description = TextField(
        DESCRIPTION_VERBOSE_NAME,
        blank=True,
        null=True
    )
    year = IntegerField(
        YEAR_VERBOSE_NAME,
        null=True,
        db_index=True
    )

    def __str__(self):
        return self.name


class Review(Model):
    """Reviews of works

    Review is linked to a specific piece of work.
    """

    text = TextField(
        REVIEW_VERBOSE_NAME,
        max_length=TEXT_MAX_LENGTH
    )
    author = ForeignKey(
        User,
        verbose_name=AUTHOR_VERBOSE_NAME,
        on_delete=CASCADE,
        related_name=REVIEW_RELATED_NAME
    )
    title = ForeignKey(
        Title,
        verbose_name=TITLE_VERBOSE_NAME,
        on_delete=CASCADE,
        related_name=REVIEW_RELATED_NAME
    )
    pub_date = DateTimeField(
        PUB_DATE_VERBOSE_NAME,
        auto_now_add=True
    )
    score = PositiveSmallIntegerField(
        SCORE_VERBOSE_NAME,
        default=SCORE_DEFAULT,
        validators=SCORE_VALIDATORS,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.title


class Comment(Model):
    """Comments on the feedback

    Comment is linked to a specific review.
    """

    text = TextField(
        COMMENT_VERBOSE_NAME,
        max_length=TEXT_MAX_LENGTH
    )
    author = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name=COMMENT_RELATED_NAME,
        verbose_name=AUTHOR_VERBOSE_NAME
    )
    review = ForeignKey(
        Review,
        on_delete=CASCADE,
        related_name=COMMENT_RELATED_NAME,
        verbose_name=REVIEW_VERBOSE_NAME
    )
    pub_date = DateTimeField(
        PUB_DATE_VERBOSE_NAME,
        auto_now_add=True
    )

    def __str__(self):
        return self.text
