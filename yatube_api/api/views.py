from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

from posts.models import Follow, Group, Post

from .permissions import IsAuthor
from .serializers import CommentSerializer, FollowSerializer, GroupSerializer
from .serializers import PostSerializer


User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет постов."""
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GrouptViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет комментариев."""
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = self.get_post()
        new_queryset = post.comments.all()
        return new_queryset

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [IsAuthenticated, ]
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)

    def get_user(self):
        return self.request.user

    def get_queryset(self):
        return Follow.objects.all().filter(
            user=self.get_user()
        )

    def perform_create(self, serializer):
        serializer.save(user=self.get_user())
