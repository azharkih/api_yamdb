from rest_framework import serializers

from api.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        fields = ['id', 'text', 'author', 'pub_date']
        model = Comment