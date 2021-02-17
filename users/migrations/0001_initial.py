# Generated by Django 3.0.5 on 2021-02-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AskRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Введите email', max_length=254, verbose_name='email')),
                ('confirmation_code', models.TextField(help_text='Введите код подтверждения', verbose_name='Код подтвержения')),
                ('ask_date', models.DateTimeField(auto_now_add=True, help_text='Укажите дату и время запроса', verbose_name='Дата запроса')),
            ],
            options={
                'verbose_name': 'Запрос на регистрацию',
                'verbose_name_plural': 'Запросы на регистрацию',
                'ordering': ['-ask_date'],
            },
        ),
    ]