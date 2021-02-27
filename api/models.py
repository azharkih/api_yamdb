from django.contrib.auth import get_user_model
from django.db import models

from api.validators import score_validator, year_validator

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Произведение',
        db_index=True,
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Слаг произведения',
    )

    class Meta:
        ordering = ('id',)


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Жанр',
        db_index=True,
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Слаг жанра',
    )

    class Meta:
        ordering = ('id',)


class Title(models.Model):
    name = models.CharField(
        verbose_name='Произведение',
        max_length=100,
        db_index=True,
    )
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        validators=[year_validator],
        db_index=True,
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='titles',
        verbose_name='Жанр',
        db_index=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Категория',
        db_index=True,
    )

    class Meta:
        ordering = ('name',)


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Заголовок отзыва',
    )
    score = models.IntegerField(
        validators=[score_validator],
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата/время отзыва',
    )

    class Meta:
        ordering = ('pub_date',)

    def __str__(self) -> str:
        return f'{self.author.username} - {self.text}'


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментируемый отзыв',
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата/время комментария',
    )

    class Meta:
        ordering = ('id',)

    def __str__(self) -> str:
        return f'{self.author.username} - {self.text}'
