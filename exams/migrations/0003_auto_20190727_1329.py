# Generated by Django 2.0.13 on 2019-07-27 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('exams', '0002_auto_20190722_0924'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useranswer',
            unique_together={('user', 'user_answer')},
        ),
    ]
