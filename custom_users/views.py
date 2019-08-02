from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import StudentForm, TeacherForm
from .models import TeacherProfile, StudentProfile

def welcome_teacher(request):
    return render(request, 'custom_users/welcome_teacher.html')

def welcome_student(request):
    return render(request, 'custom_users/welcome_student.html')

def signup(request):
    return render(request, 'signup.html')

def signup_form_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            StudentProfile.objects.create(user = user)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('welcome_student')
    else:
        form = StudentForm()
    return render(request, 'signup_form_student.html', {'form': form})

def signup_form_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            TeacherProfile.objects.create(user = user)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('welcome_teacher')
    else:
        form = TeacherForm()
    return render(request, 'signup_form_teacher.html', {'form': form})
