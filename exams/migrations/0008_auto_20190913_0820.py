# Generated by Django 2.0.13 on 2019-09-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_question_questiongif'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questionreviewimage',
            new_name='reviewgif',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='questionreviewscript',
            new_name='reviewimage',
        ),
        migrations.AddField(
            model_name='question',
            name='reviewscript',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
