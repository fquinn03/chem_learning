from django.db import models

"""
Lesson has level and tile 
Lesson contains link to resource embed code.
This code must be filtered as |safe in template
"""
class Lesson(models.Model):
    level = models.IntegerField(default = 1)
    title = models.CharField(max_length = 100, unique = True)
    link = models.CharField(max_length = 500)
    def __str__(self):
        return self.title
