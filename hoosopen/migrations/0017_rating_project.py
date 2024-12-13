# Generated by Django 4.2.16 on 2024-11-12 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("hoosopen", "0016_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="project",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ratings",
                to="hoosopen.project",
            ),
            preserve_default=False,
        ),
    ]