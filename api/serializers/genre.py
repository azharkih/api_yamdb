from rest_framework import serializers

from ..models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Genre
