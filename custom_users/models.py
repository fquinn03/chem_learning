from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from lessons.models import Lesson

# School details Name and PostCode Required
class School(models.Model):
    name = models.CharField(max_length=100, unique = True)
    post_code = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name+", "+self.post_code
"""
Created when users signups up as teacher
School and class_id are updated through edit_teacher at signup
Details added flag is changed to True when this is completed.
"""
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    is_teacher = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null = True)
    details_added = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# One teacher can have many classes, can be named by user.
class Class_id(models.Model):
    name = models.CharField(max_length=100, default="My Class")
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

"""
Created when user signups up as student.
School, Teacher and class_id are updated through edit_student at signup
Details added flag is changed to True when this is completed.
Level is updated after user completes signup_quiz at signup
Signup_quiz_completed flag is changed to True when this is completed.
"""
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null = True)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, blank=True, null = True)
    class_id = models.ForeignKey(Class_id, on_delete=models.CASCADE, blank=True, null = True)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    level = models.IntegerField(default=1)
    attempt = models.IntegerField(default=1)
    next_lesson_id = models.IntegerField(default=1)
    completed_lessons = models.ManyToManyField(Lesson)
    details_added = models.BooleanField(default=False)
    signup_quiz_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
