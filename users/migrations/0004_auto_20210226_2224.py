# Generated by Django 3.0.5 on 2021-02-26 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210218_2146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',)},
        ),
    ]
