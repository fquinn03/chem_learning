# Generated by Django 2.0.13 on 2019-09-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20190905_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionreview',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
