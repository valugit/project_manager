# Generated by Django 2.2.6 on 2019-10-21 12:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20191021_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(2024), django.core.validators.MinValueValidator(2014)]),
        ),
    ]
