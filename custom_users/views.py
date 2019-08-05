from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import StudentForm, TeacherForm
from .models import Class_id, TeacherProfile, StudentProfile

def welcome_teacher(request):
    return render(request, 'custom_users/welcome_teacher.html')

def welcome_student(request):
    user = request.user
    student = StudentProfile.objects.select_related().get(user_id = user.id)
    level = student.level.__str__()
    return render(request, 'custom_users/welcome_student.html', {'user':user,
    'level':level})

def signup(request):
    return render(request, 'signup.html')

def signup_form_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            student = StudentProfile.objects.create(user=user)
            student = student.select_related("level")
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('welcome_student', {'student': student })
    else:
        form=StudentForm()
    return render(request, 'signup_form_student.html', {'form': form})

def signup_form_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            TeacherProfile.objects.create(user=user)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('welcome_teacher')
    else:
        form=TeacherForm()
    return render(request, 'signup_form_teacher.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.select_related().get(user_id = request.user.id)
            level = student.level.__str__()
            if student:
                return render(request, 'custom_users/welcome_student.html', {'level':level})
        except:
            teacher = TeacherProfile.objects.get(user_id = request.user.id)
            classes = Class_id.objects.filter(teacher = teacher)
            if teacher:
                return render(request, 'custom_users/welcome_teacher.html',{'classes':classes})
    else:
            return render(request, 'signup.html')
