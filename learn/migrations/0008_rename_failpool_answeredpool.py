# Generated by Django 4.0.1 on 2022-01-30 09:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learn', '0007_failpool_answers_failpool_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FailPool',
            new_name='AnsweredPool',
        ),
    ]
