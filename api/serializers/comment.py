from rest_framework import serializers

from api.models import Comment, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault())

    class Meta:
        fields = ['id', 'text', 'author', 'pub_date']
        model = Comment
