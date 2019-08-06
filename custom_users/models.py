from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class School(models.Model):
    name = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name+", "+self.post_code

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    is_teacher = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null = True)

    def __str__(self):
        return self.user.username

class Class_id(models.Model):
    name = models.CharField(max_length=100, default="My Class")
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null = True)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, blank=True, null = True)
    class_id = models.ForeignKey(Class_id, on_delete=models.CASCADE, blank=True, null = True)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    level = models.IntegerField(default=1)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
