# Generated by Django 2.0.13 on 2019-09-05 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionimage',
            field=models.CharField(default='imagelink', max_length=250),
            preserve_default=False,
        ),
    ]