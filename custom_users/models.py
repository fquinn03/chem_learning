from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_teacher = models.BooleanField(default = True)
    is_student = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username

class Class_id(models.Model):
    name = models.CharField(max_length = 100, default = "My Class")
    teacher = models.ForeignKey(TeacherProfile, on_delete = models.CASCADE)

    def __str__(self):
        return self.name+" "+ str(self.teacher)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher = models.ForeignKey(TeacherProfile, on_delete = models.CASCADE, blank=True, null=True)
    class_id = models.ForeignKey(Class_id, on_delete = models.CASCADE, blank=True, null=True)
    is_student = models.BooleanField(default = True)
    is_teacher = models.BooleanField(default = False)
    level = models.IntegerField(default = 1)
    score = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.username
"""
@receiver(post_save, sender=User)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created:
        TeacherProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if isinstance(instance, TeacherProfile):
        instance.teacherprofile.save()
    else:
        instance.studentprofile.save()
"""
