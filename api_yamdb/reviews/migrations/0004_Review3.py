# Generated by Django 3.2 on 2023-05-18 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_Review2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='score',
        ),
    ]