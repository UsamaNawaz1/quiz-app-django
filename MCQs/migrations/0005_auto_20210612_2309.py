# Generated by Django 3.1.6 on 2021-06-12 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCQs', '0004_auto_20210612_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempts',
            name='on_quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizattempts', to='MCQs.quiz'),
        ),
    ]
