from django.shortcuts import render
from users.models import User

def welcome_teacher(request):
    return render(request, 'users/welcome_teacher.html', {
    })


def welcome_student(request):
    return render(request, 'users/welcome_student.html', {
    })
