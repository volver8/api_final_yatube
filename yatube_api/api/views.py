from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
    DjangoObjectPermissions,
    IsAuthenticatedOrReadOnly
)

from posts.models import Group, Post
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from .viewsets import ListCreateView


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет постов."""
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GrouptViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет групп."""
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет комментариев."""
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(ListCreateView):
    permission_classes = (IsAuthenticated, )
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follows

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
