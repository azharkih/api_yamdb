from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import AskRegistrationSerializer, StatusSerializer
from .registration import registration


class AskRegistrationView(APIView):
    def post(self, request):
        in_serializer = AskRegistrationSerializer(data=request.data)
        if in_serializer.is_valid():
            email = in_serializer.validated_data['email']
            code = registration(email)
            status_info = StatusSerializer(
                {'status_info': f'Отправлен код на {email}'}
            )
        else:
            status_info = StatusSerializer({'status_info': 'емейл не валидный'})
        return Response(status_info.data, status=status.HTTP_200_OK)
