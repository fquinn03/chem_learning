from django.shortcuts import render
from .models import StudentProfile, Class_id


def show_students(request, class_name, teacher_id):
    group = Class_id.objects.get(name = class_name, teacher = teacher_id)
    students = StudentProfile.objects.all().filter(class_id = group.id)
    return render(request, 'users/show_students.html', {
    'group': group,
    'students': students,
    })

def welcome(request):
    return render(request, 'users/welcome.html')
