# Generated by Django 4.2.16 on 2024-10-08 18:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('join_date', models.DateField(default=datetime.date.today)),
                ('bio', models.CharField(default='Show your personality by adding a fun bio!', max_length=5000, null=True)),
                ('github_username', models.CharField(max_length=39, null=True)),
                ('graduation_year', models.IntegerField(choices=[(2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029)], null=True)),
                ('graduation_semester', models.CharField(choices=[(1, 'Spring'), (2, 'Fall')], max_length=10, null=True)),
                ('interests', models.CharField(default='Nothing here so far...', max_length=5000, null=True)),
                ('skills', models.CharField(default='Nothing here so far...', max_length=5000, null=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency', models.CharField(choices=[('novice', 'Novice - No prior experience or knowledge.'), ('beginner', 'Beginner - Basic understanding but limited practical experience.'), ('intermediate', 'Intermediate - Working knowledge with some practical experience.'), ('advanced', 'Advanced - Proficient with substantial practical experience.'), ('expert', 'Expert - Deep expertise and can mentor others.')], default=('novice', 'Novice - No prior experience or knowledge.'), max_length=100)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoosopen.skill')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoosopen.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.CharField(max_length=5000)),
                ('application_required', models.BooleanField(default=False)),
                ('location', models.CharField(choices=[('inperson', 'In-Person'), ('online', 'Online'), ('hybrid', 'Hybrid')], default=('inperson', 'In-Person'), max_length=100)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='hoosopen.userprofile')),
                ('members', models.ManyToManyField(blank=True, related_name='members', to='hoosopen.userprofile')),
                ('skills', models.ManyToManyField(blank=True, to='hoosopen.skill')),
                ('tags', models.ManyToManyField(blank=True, to='hoosopen.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(choices=[('github', 'GitHub'), ('discord', 'Discord'), ('slack', 'Slack'), ('googledrive', 'Google Drive'), ('other', 'Other')], max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hoosopen.project')),
            ],
        ),
    ]