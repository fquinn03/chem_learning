# Generated by Django 2.0.13 on 2019-09-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_question_questionreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionreviewscript',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='questionscript',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]