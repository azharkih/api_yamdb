from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.view import (
    AskRegistrationView, TokenView, UserViewSet)

router = DefaultRouter()

router.register('v1/users', UserViewSet)

urlpatterns = [
    path('v1/auth/email/', AskRegistrationView.as_view(),
         name='send_code'),
    path('v1/token/', TokenView.as_view(),
         name='token_obtain_pair'),
    path('', include(router.urls)),
]
