# Generated by Django 3.1.6 on 2021-06-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]