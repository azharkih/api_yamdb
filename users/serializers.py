from rest_framework import serializers

from .models import AskRegistration


class AskRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()


class StatusSerializer(serializers.Serializer):
    status_info = serializers.CharField()
