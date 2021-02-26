from rest_framework import serializers

from ..models.review import Review
from ..models.user import User


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
        similar_review = Review.objects.filter(author=data['author'],
                                               title=title).first()
        if similar_review:
            raise serializers.ValidationError(
                    'Вы можете оставить только один отзыв')
        score = data['score']
        if score <= 0 or score > 10:
            raise serializers.ValidationError(
                    'Рейтинг может быть в диапозоне от 1 до 10'
            )
        return data