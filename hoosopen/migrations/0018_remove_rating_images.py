# Generated by Django 4.2.16 on 2024-11-14 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoosopen', '0017_rating_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='images',
        ),
    ]