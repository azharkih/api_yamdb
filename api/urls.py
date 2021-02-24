from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.genre import GenreViewSet
from .views.category import CategoryViewSet
from .views.title import TitleViewSet

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='post')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
]
