# Generated by Django 3.0.5 on 2021-02-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('email',
                 models.EmailField(help_text='Введите email', max_length=254,
                                   verbose_name='email')),
                ('confirmation_code',
                 models.TextField(help_text='Введите код подтверждения',
                                  verbose_name='Код подтвержения')),
                ('ask_date', models.DateTimeField(auto_now_add=True,
                                                  help_text='Укажите дату и время запроса',
                                                  verbose_name='Дата запроса')),
            ],
            options={
                'verbose_name': 'Запрос на регистрацию',
                'verbose_name_plural': 'Запросы на регистрацию',
                'ordering': ['-ask_date'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('password',
                 models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True,
                                                    verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username',
                 models.CharField(db_index=True, max_length=255, unique=True)),
                ('bio', models.CharField(max_length=1000)),
                ('email',
                 models.EmailField(db_index=True, max_length=254, unique=True)),
                ('role', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set',
                                                  related_query_name='user',
                                                  to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True,
                                                            help_text='Specific permissions for this user.',
                                                            related_name='user_set',
                                                            related_query_name='user',
                                                            to='auth.Permission',
                                                            verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
