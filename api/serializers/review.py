from rest_framework import serializers

from api.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    
    def validate(self, data):
        if Review.objects.filter(
            title=self.context['view'].kwargs.get('title_id'),
            author=self.context['request']._user and self.context['request'].method == 'POST'
        ).exists():
                raise serializers.ValidationError(
                    'Вы можете оставить только один отзыв'
                )
        score = data['score']
        if score <= 0 or score > 10:
            raise serializers.ValidationError(
                'Рейтинг может быть в диапозоне от 1 до 10'
            )
        return data

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        model = Review