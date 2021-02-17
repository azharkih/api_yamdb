from django.urls import path

from .views.main import AskRegistrationView

urlpatterns = [
    path('v1/auth/email/', AskRegistrationView.as_view(),
         name='send_code'),
]
