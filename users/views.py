from django.contrib.auth import get_user_model
from django.shortcuts import render
from users.models import User

User = get_user_model()

def welcome_teacher(request):
    return render(request, 'users/welcome_teacher.html', {
    })


def welcome_student(request):
    return render(request, 'users/welcome_student.html', {
    })
