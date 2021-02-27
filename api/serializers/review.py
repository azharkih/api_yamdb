from rest_framework import serializers

from users.models import User
from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault())

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        model = Review

    def validate(self, data):
        title = self.context['view'].kwargs.get('title_id')
        author = self.context['request'].user

        if self.context['request'].method == 'POST':
            similar_review = Review.objects.filter(author=author,
                                                   title=title).exists()
            if similar_review:
                raise serializers.ValidationError(
                    'Вы можете оставить только один отзыв')
        return data
