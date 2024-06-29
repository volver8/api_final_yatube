from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post
from .models import Group  # , Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('__all__')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    slug = serializers.SlugRelatedField(
        read_only=True, slug_field='slug'
    )

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


# class FollowSerializer(serializers.ModelSerializer):
#     slug = serializers.SlugRelatedField(
#         read_only=True, slug_field='slug'
#     )

#     class Meta:
#         fields = '__all__'
#         model = Group
