# Generated by Django 2.0.13 on 2019-08-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0002_auto_20190815_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='starting_level',
            field=models.IntegerField(default=1),
        ),
    ]
