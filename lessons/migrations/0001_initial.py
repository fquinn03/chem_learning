# Generated by Django 2.0.13 on 2019-08-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('link', models.CharField(max_length=500)),
                ('image_link', models.CharField(default='lesson_image_link', max_length=500)),
            ],
        ),
    ]
