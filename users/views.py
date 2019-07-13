from django.shortcuts import render
from .models import StudentProfile, Class_id


def show_students(request, class_name):
    group = Class_id.objects.get(name = class_name)
    students = StudentProfile.objects.all().filter(class_id = group.id)
    return render(request, 'users/show_students.html', {
    'group': group,
    'students': students,
    })

def welcome(request):
    return render(request, 'users/welcome.html')
