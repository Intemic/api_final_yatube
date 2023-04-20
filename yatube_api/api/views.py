from rest_framework.viewsets import ModelViewSet

from rest_framework.pagination import LimitOffsetPagination
from posts.models import Post
from .permissions import OwnerOrReadOnly, ReadOnly
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
