# Generated by Django 3.1.6 on 2021-06-12 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCQs', '0003_attempts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempts',
            name='on_quiz',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quizattempts', to='MCQs.quiz'),
        ),
    ]
