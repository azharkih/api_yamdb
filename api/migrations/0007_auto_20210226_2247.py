# Generated by Django 3.0.5 on 2021-02-26 19:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20210226_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100,
                                   verbose_name='Произведение'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True,
                                   verbose_name='Слаг произведения'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='comments',
                                    to=settings.AUTH_USER_MODEL,
                                    verbose_name='Автор комментария'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата/время комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(default=1,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='comments', to='api.Review',
                                    verbose_name='Комментируемый отзыв'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(max_length=100, unique=True,
                                   verbose_name='Слаг жанра'),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='reviews',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Автор отзыва'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата/время отзыва'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(default=1,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='reviews', to='api.Title',
                                    verbose_name='Заголовок отзыва'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='titles', to='api.Category',
                                    verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='titles',
                                         to='api.Genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(max_length=100,
                                   verbose_name='Произведение'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveIntegerField(verbose_name='Год выпуска'),
        ),
    ]
