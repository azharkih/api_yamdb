# Generated by Django 3.0.5 on 2021-02-27 07:52

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210226_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Произведение'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=1, validators=[api.validators.score_validator]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='titles', to='api.Genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Произведение'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveIntegerField(db_index=True, validators=[api.validators.year_validator], verbose_name='Год выпуска'),
        ),
    ]