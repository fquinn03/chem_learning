# Generated by Django 2.0.13 on 2019-08-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0003_auto_20190810_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='next_lesson_name',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='next_lesson_id',
            field=models.IntegerField(default=1),
        ),
    ]
