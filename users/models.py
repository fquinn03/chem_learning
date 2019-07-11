
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Class_id(models.Model):
    name = models.CharField(max_length = 100, default = "class_name")
    teacher = models.ForeignKey(TeacherProfile, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher = models.ForeignKey(TeacherProfile, on_delete = models.CASCADE)
    class_id = models.ForeignKey(Class_id, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username
