# Generated by Django 4.2.16 on 2024-10-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoosopen', '0005_alter_message_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
