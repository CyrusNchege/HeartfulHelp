# Generated by Django 5.0 on 2024-01-15 09:03

import donations.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_alter_fundraisecause_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundraisecause',
            name='image',
            field=models.ImageField(blank=True, default=donations.models.default_image, null=True, upload_to='cause_images'),
        ),
    ]
