# Generated by Django 5.1.2 on 2025-02-21 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_expertuser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expertuser',
            old_name='username',
            new_name='yourusername',
        ),
    ]
