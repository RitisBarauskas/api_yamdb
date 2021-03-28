from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet
from random import choices
from string import digits, ascii_uppercase


def generate_confirmation_code(length):
    return ''.join(choices(digits + ascii_uppercase, k=length))


class ObjectViewSetMixin(ListModelMixin,
                         CreateModelMixin,
                         DestroyModelMixin,
                         GenericViewSet):
    pass
