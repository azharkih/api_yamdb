from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken

from .models import AskRegistration, User


class AskRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()


class StatusSerializer(serializers.Serializer):
    status_info = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    """ Класс TokenSerializer описывает сериализатор выдачи токена.

    Родительский класс -- serializers.ModelSerializer.
    """

    email = serializers.EmailField(write_only=True)
    confirmation_code = serializers.CharField(
        max_length=10, min_length=10, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        if not AskRegistration.objects.get(
                email=data['email'],
                confirmation_code=data['confirmation_code']
        ):
            raise serializers.ValidationError('Неверный код подтверждения')
        return data

    def create(self, validated_data):
        email = validated_data['email']
        values = {'email': email, 'username': email}
        user, created = User.objects.get_or_create(email=email, defaults=values)
        token = AccessToken.for_user(user)
        validated_data['token'] = token
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role')
        model = User
