from django.db import models
from users.models import StudentProfile


class Level(models.Model):
    title = models.CharField(max_length = 100)
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

class Exam(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    number = models.IntegerField()

    class Meta:
        unique_together = ('level', 'number', )

    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    number = models.IntegerField(default = 1)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    correct = models.BooleanField()

    def __str__(self):
        return self.text

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('question', 'user', )

    def __str__(self):
        return self.answer
