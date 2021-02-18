from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import AskRegistrationSerializer, StatusSerializer, \
    TokenSerializer, UserSerializer
from .registration import registration
from ..models import User


class AskRegistrationView(APIView):
    def post(self, request):
        in_serializer = AskRegistrationSerializer(data=request.data)
        if in_serializer.is_valid():
            email = in_serializer.validated_data['email']
            registration(email)
            status_info = StatusSerializer(
                {'status_info': f'Отправлен код на {email}'}
            )
        else:
            status_info = StatusSerializer({'status_info': 'емейл не валидный'})
        return Response(status_info.data, status=status.HTTP_200_OK)


class TokenView(APIView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    Класс UserViewSet используется для обработки api-запросов на операции
    CRUD модели User.

    Родительский класс -- viewsets.ModelViewSet.
    Переопределенные атрибуты -- queryset, serializer_class,
    permission_classes, lookup_field.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]
