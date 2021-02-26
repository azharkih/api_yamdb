from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from ..models import Category
from ..models import Genre
from ..models import Title
from .genre import GenreSerializer
from .category import CategorySerializer


class TitleSerializerGet(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                         slug_field='slug',
                                         many=True)
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field='slug')

    class Meta:
        fields = '__all__'
        model = Title
