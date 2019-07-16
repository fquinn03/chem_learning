from django.db import models
from exams.models import Level

class Lesson(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    link = models.CharField(max_length = 500)
    number = models.IntegerField()

    def __str__(self):
        return self.title
