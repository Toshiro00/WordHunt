# Generated by Django 4.0.1 on 2022-01-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_alter_wordpool_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordpool',
            name='language',
            field=models.CharField(default='', max_length=10),
        ),
    ]
