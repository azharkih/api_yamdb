from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import get_object_or_404
from api.permissions.review import IsAuthorOrAdminOrModeratorOrReadOnly

from api.models.comment import Comment
from api.models.review import Review

from api.serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthorOrAdminOrModeratorOrReadOnly,
                        IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(
            Review, pk=self.kwargs.get('review_id')
        )
        return review.comments.all()

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(author=self.request.user)
        
        