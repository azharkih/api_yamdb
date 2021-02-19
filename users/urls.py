from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.main import (
    AskRegistrationView, OwnUserViewSet, TokenView, UserViewSet)

router = DefaultRouter()

router.register('v1/users', UserViewSet)

urlpatterns = [
    path('v1/auth/email/', AskRegistrationView.as_view(),
         name='send_code'),
    path('v1/token/', TokenView.as_view(),
         name='token_obtain_pair'),
    path('v1/users/me/', OwnUserViewSet.as_view(),
         name='own_user'),
    path('', include(router.urls)),
]
