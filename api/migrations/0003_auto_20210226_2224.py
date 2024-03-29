# Generated by Django 3.0.5 on 2021-02-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_auto_20210226_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата добавления'),
        ),
    ]
