from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import Comment
from api.models import Review
from api.permissions.review import IsAuthorOrAdminOrModeratorOrReadOnly
from api.serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrAdminOrModeratorOrReadOnly,
                          IsAuthenticatedOrReadOnly]

    @property
    def review(self):
        title_id = self.kwargs.get("title_id")
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review.objects.filter(title_id=title_id),
                                   id=review_id)
        return review

    def get_queryset(self):
        return Comment.objects.filter(review=self.review)

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(review=self.review)
