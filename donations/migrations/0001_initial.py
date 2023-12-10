# Generated by Django 5.0 on 2023-12-10 11:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FundraiseCause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('goal', models.IntegerField()),
                ('current_amount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('account_number', models.IntegerField()),
                ('image', models.ImageField(blank=True, default='cause_images/default.webp', null=True, upload_to='cause_images')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.IntegerField()),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='donations.fundraisecause')),
            ],
        ),
    ]