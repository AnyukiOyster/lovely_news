# Generated by Django 5.1.4 on 2024-12-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_image_subtext',
            field=models.CharField(default=0, max_length=512),
            preserve_default=False,
        ),
    ]
