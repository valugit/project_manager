# Generated by Django 2.2.6 on 2019-10-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20191027_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
