# Generated by Django 2.2.6 on 2019-10-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.IntegerField(default=2022),
            preserve_default=False,
        ),
    ]