# Generated by Django 2.0.13 on 2019-08-10 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0004_auto_20190810_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='completed_lessons',
            field=models.ManyToManyField(null=True, to='lessons.Lesson'),
        ),
    ]
