# Generated by Django 2.2.6 on 2019-10-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_projectgroup_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='Herbert Jean-Guy', max_length=255),
            preserve_default=False,
        ),
    ]
