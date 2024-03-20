from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """ Docstring """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        comments_count = Count(
            'comment', distinct=True
        ),
        likes_count = Count(
            'likes', distinct=True
        ),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        # user feed
        'owner__followed__owner__profile',
        # user likes posts
        'likes__owner__profile',
        # user posts
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Docstring """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('comment', distinct=True)
    ).order_by('-created_at')