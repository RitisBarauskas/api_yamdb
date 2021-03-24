from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet


class ObjectViwSetMixin(CreateModelMixin, ListModelMixin, GenericViewSet):
    pass
