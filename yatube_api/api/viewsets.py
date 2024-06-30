from rest_framework import mixins, viewsets


class ListCreateView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass
