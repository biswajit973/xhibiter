# Generated by Django 5.1.2 on 2025-04-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_servicevideoform_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingstatus',
            name='booking_timezone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
