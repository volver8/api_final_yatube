from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GrouptViewSet, PostViewSet

router_v1 = DefaultRouter()

router_v1.register(
    'posts',
    PostViewSet,
    basename='posts'
)
router_v1.register(
    'groups',
    GrouptViewSet,
    basename='groups'
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(
    'follow',
    FollowViewSet,
    basename='follows'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
