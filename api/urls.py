from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.genre import GenreViewSet
from .views.category import CategoryViewSet

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='post')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router.urls)),
]
