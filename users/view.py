from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.permissions import IsAdmin, IsOwner
from users.registration import registration
from users.serializers import (
    AskRegistrationSerializer, StatusSerializer, TokenSerializer,
    UserSerializer)


class AskRegistrationView(APIView):
    """
    Класс AskRegistrationView используется для обработки api-запросов на
    регистрацию пользователя.

    Поддерживаются только post-запросы.
    """

    def post(self, request):
        in_serializer = AskRegistrationSerializer(data=request.data)
        if in_serializer.is_valid():
            email = in_serializer.validated_data['email']
            registration(email)
            status_info = StatusSerializer(
                {'status_info': f'Отправлен код на {email}'}
            )
        else:
            status_info = StatusSerializer(
                {'status_info': 'емейл не валидный'})
        return Response(status_info.data, status=status.HTTP_200_OK)


class TokenView(APIView):
    """
    Класс TokenView используется для обработки api-запросов на получение
    токена.

    Поддерживаются только post-запросы.
    """

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    """
    Класс UserViewSet используется для обработки api-запросов на операции CRUD
    модели User.

    Родительский класс -- viewsets.ModelViewSet.
    Переопределенные атрибуты -- queryset, serializer_class,
    permission_classes, lookup_field.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAdmin]

    @action(detail=False, methods=['get', 'patch'],
            permission_classes=[IsOwner])
    def me(self, request):
        if self.request.method == 'PATCH':
            instance = self.request.user
            serializer = self.get_serializer(instance, data=request.data,
                                             partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
