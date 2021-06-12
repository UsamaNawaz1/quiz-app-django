# Generated by Django 3.1.6 on 2021-06-12 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0007_remove_userprofile_attempts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempts', models.IntegerField(default=0)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='lesson.userprofile')),
                ('on_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizattempts', to='lesson.lesson')),
            ],
        ),
    ]