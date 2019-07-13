from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length = 100)
    link = models.CharField(max_length = 500)
    level = models.IntegerField()

    def __str__(self):
        return self.title
