# Generated by Django 5.1.2 on 2025-04-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_bookingstatus_session_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicevideoform',
            name='bufferTime',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='servicevideoform',
            name='maxBookings',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
