from django.db import models
from custom_users.models import StudentProfile


class Level(models.Model):
    title = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.id)

class Exam(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)

    class Meta:
        unique_together = ('level', 'id', )
    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    def __str__(self):
        return self.text

class Written_Question(Question):
    is_written = models.BooleanField(default = True)

    class Meta:
        verbose_name="Written_Question"

class MCQ_Question(Question):
    is_MCQ = models.BooleanField(default = True)

    class Meta:
        verbose_name="MCQ_Question"

class Formula_Question(Question):
    is_formula = models.BooleanField(default = True)

    class Meta:
        verbose_name="Formula_Question"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    correct = models.BooleanField(default = False)
    correct_spelling = models.BooleanField(default = True)

    def __str__(self):
        return self.text

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=1000)
    user = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'user_answer' )
    def __str__(self):
        return self.user_answer
