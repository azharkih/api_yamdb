from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.category import CategoryViewSet
from .views.comment import CommentViewSet
from .views.genre import GenreViewSet
from .views.review import ReviewViewSet
from .views.title import TitleViewSet

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='post')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
]
