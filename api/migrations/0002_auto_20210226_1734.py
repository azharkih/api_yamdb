# Generated by Django 3.0.5 on 2021-02-26 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True,
                                       help_text='Укажите дату и отзыва',
                                       verbose_name='Дата/время отзыва'),
        ),
    ]
