from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)


class Title(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='titles', blank=True, null=True)
    genre = models.ManyToManyField(Genre, related_name='titles', blank=True)
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    description = models.TextField()


class Review(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE, blank=True, null=True,
                               related_name="reviews")
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE, related_name="reviews",
                              blank=True, null=True)
    score = models.IntegerField(null=True)
    text = models.TextField()
    pub_date = models.DateTimeField(
        verbose_name='Дата/время отзыва',
        auto_now_add=True,
        help_text='Укажите дату и отзыва'
    )

    def __str__(self) -> str:
        return f'{self.author.username} - {self.text}'


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE, blank=True, null=True,
                               related_name="comments")
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name="comments", blank=True, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField("Дата добавления",
                                    auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author.username} - {self.text}'
