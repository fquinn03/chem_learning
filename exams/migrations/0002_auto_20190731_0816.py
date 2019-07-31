# Generated by Django 2.0.13 on 2019-07-31 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.StudentProfile'),
        ),
        migrations.AddField(
            model_name='question',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Exam'),
        ),
        migrations.AddField(
            model_name='exam',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Level'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='useranswer',
            unique_together={('user', 'user_answer')},
        ),
        migrations.AlterUniqueTogether(
            name='exam',
            unique_together={('level', 'id')},
        ),
    ]