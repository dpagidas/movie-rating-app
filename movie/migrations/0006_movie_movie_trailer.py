# Generated by Django 2.2.4 on 2019-09-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
