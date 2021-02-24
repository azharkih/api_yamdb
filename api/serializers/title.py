from rest_framework import serializers

from ..models.title import Title
from ..serializers.genre import GenreSerializer
from ..serializers.category import CategorySerializer


class TitleSerializerGet(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer(read_only=True)
#    rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title
