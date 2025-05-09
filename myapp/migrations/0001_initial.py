# Generated by Django 5.1.2 on 2025-04-21 07:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.IntegerField(blank=True, null=True)),
                ('session_name', models.CharField(blank=True, max_length=7, null=True)),
                ('selectedTime', models.TimeField(blank=True, null=True)),
                ('selectedDate', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=7, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('expert_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('youtubelink', models.URLField(blank=True, max_length=300, null=True)),
                ('instagramlink', models.URLField(blank=True, max_length=300, null=True)),
                ('subscribersCount', models.BigIntegerField(blank=True, null=True)),
                ('followersCount', models.BigIntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_expert', models.BooleanField(default=False)),
                ('delete1', models.IntegerField(default=0)),
                ('yourusername', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('displayname', models.CharField(blank=True, max_length=100, null=True)),
                ('introduction', models.CharField(blank=True, max_length=500, null=True)),
                ('aboutyourself', models.CharField(blank=True, max_length=500, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('personalAddress', models.CharField(blank=True, max_length=500, null=True)),
                ('officeAddress', models.CharField(blank=True, max_length=500, null=True)),
                ('alternateContactNumber', models.CharField(blank=True, max_length=11, null=True)),
                ('alternateEmail', models.CharField(blank=True, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServicePriorityDmForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('amount', models.CharField(blank=True, max_length=7, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceVideoForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('duration', models.CharField(blank=True, max_length=2, null=True)),
                ('amount', models.CharField(blank=True, max_length=7, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceWebinarForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('duration', models.CharField(blank=True, max_length=2, null=True)),
                ('session_time', models.TimeField(blank=True, null=True)),
                ('session_date', models.DateField(blank=True, null=True)),
                ('amount', models.CharField(blank=True, max_length=7, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
