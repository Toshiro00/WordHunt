# Generated by Django 4.0.1 on 2022-01-29 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordpool',
            name='user',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
