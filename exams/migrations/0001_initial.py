# Generated by Django 2.0.13 on 2019-08-10 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('correct', models.BooleanField(default=False)),
                ('correct_spelling', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('percentage', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('level', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Formula_Question',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exams.Question')),
                ('is_formula', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Formula_Question',
            },
            bases=('exams.question',),
        ),
        migrations.CreateModel(
            name='MCQ_Question',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exams.Question')),
                ('is_MCQ', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'MCQ_Question',
            },
            bases=('exams.question',),
        ),
        migrations.CreateModel(
            name='Written_Question',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exams.Question')),
                ('is_written', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Written_Question',
            },
            bases=('exams.question',),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Question'),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_users.StudentProfile'),
        ),
        migrations.AddField(
            model_name='question',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Exam'),
        ),
        migrations.AddField(
            model_name='completedexam',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Exam'),
        ),
        migrations.AddField(
            model_name='completedexam',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_users.StudentProfile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Question'),
        ),
    ]
