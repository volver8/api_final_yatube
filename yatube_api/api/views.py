from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post
from .permissions import IsAuthor


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет постов."""
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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
