from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import get_object_or_404
from api.permissions.review import IsAuthorOrAdminOrModeratorOrReadOnly

from api.models import Comment, Title
from api.models import Review

from api.serializers.comment import CommentSerializer
from users.permissions import IsAdminOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # pagination_class = PageNumberPagination
    # permission_classes_by_action = {'create': [AllowAny],
    #                                 'list'  : [IsAdminUser]}
    permission_classes = [IsAuthorOrAdminOrModeratorOrReadOnly,
                          IsAuthenticatedOrReadOnly]

    # def get_permission_classes(self):
    #     pass

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review.objects.filter(title_id=title_id),
                                   id=review_id)
        return Comment.objects.filter(review=review)

    def perform_create(self, serializer, *args, **kwargs):
        title_id = self.kwargs.get("title_id")
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review.objects.filter(title_id=title_id),
                                   id=review_id)
        serializer.save(review=review)
