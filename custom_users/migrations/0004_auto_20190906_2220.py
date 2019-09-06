# Generated by Django 2.0.13 on 2019-09-06 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0003_auto_20190906_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_users.Class_id'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_users.School'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_users.TeacherProfile'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_users.School'),
        ),
    ]