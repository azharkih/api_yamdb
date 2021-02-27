from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken

from api_yamdb import settings
from .models import AskRegistration, User


class AskRegistrationSerializer(serializers.Serializer):
    """ Класс AskRegistrationSerializer описывает сериализатор данных запроса на
    регистрацию.

    Родительский класс -- serializers.Serializer.
    """

    email = serializers.EmailField()


class StatusSerializer(serializers.Serializer):
    """ Класс StatusSerializer описывает сериализатор данных статусных ответов.

    Родительский класс -- serializers.Serializer.
    """

    status_info = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    """ Класс TokenSerializer описывает сериализатор выдачи токена.

    Родительский класс -- serializers.Serializer.
    """
    length = settings.LENGTH_CONFIRMATION_CODE

    email = serializers.EmailField(write_only=True)
    confirmation_code = serializers.CharField(
        max_length=length, min_length=length, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        if not AskRegistration.objects.filter(
            email=data['email'],
            confirmation_code=data['confirmation_code']
        ).exists():
            raise serializers.ValidationError('Неверный код подтверждения')
        return data

    def create(self, validated_data):
        email = validated_data['email']
        values = {'email': email, 'username': email}
        user, created = User.objects.get_or_create(email=email,
                                                   defaults=values)
        token = AccessToken.for_user(user)
        validated_data['token'] = token
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    """ Класс UserSerializer описывает сериализатор данных запроса на основе
    модели User.

    Родительский класс -- serializers.ModelSerializer.
    """

    class Meta:
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role')
        model = User
