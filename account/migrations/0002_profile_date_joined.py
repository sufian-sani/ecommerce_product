# Generated by Django 3.1 on 2022-04-30 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
