# Generated by Django 2.0.13 on 2019-07-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20190715_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]