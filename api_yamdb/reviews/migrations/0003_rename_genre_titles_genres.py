# Generated by Django 3.2 on 2023-05-19 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_rename_genres_titles_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='titles',
            old_name='genre',
            new_name='genres',
        ),
    ]
