from rest_framework import serializers

from api.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        fields = '__all__'
        model = Comment