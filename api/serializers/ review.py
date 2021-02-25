from rest_framework import serializers

from api.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        fields = '__all__'
        model = Review
