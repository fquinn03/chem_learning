# Generated by Django 2.0.13 on 2019-08-12 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0002_studentprofile_next_exam_id'),
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useranswer',
            unique_together={('user', 'user_answer')},
        ),
    ]
