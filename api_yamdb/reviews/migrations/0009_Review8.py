# Generated by Django 3.2 on 2023-05-18 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_Review7'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title_id',
            new_name='title',
        ),
    ]