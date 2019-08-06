from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import StudentForm, TeacherForm, StudentProfileForm
from .models import Class_id, School, TeacherProfile, StudentProfile

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
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('welcome_student')
    else:
        form=StudentForm()
    return render(request, 'signup_form_student.html', {'form': form})

def signup_form_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            TeacherProfile.objects.create(user=user, school = 1)
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

def edit_student(request):
    if request.method == 'POST':
        user = request.user
        student = get_object_or_404(StudentProfile, user_id = user.id)
        form = StudentProfileForm(request.POST, instance = student)
        if form.is_valid():
            form = form.save()
            return render(request, 'custom_users/student_details_added.html', {'student':student})
    else:
        form=StudentProfileForm()
    return render(request, 'custom_users/edit_student.html', {'form': form})

def student_details_added(request):
    student = StudentProfile.objects.get(user_id = request.user.id)
    return render(request, 'custom_users/student_details_added.html', {'student': student})

def ajax_load_teachers(request):
    school_id = request.GET.get('school')
    teachers = TeacherProfile.objects.filter(school=school_id).order_by('user_id')
    return render(request, 'custom_users/ajax_load_teachers.html', {'teachers': teachers})

def ajax_load_classes(request):
    teacher_id = request.GET.get('teacher')
    class_ids = Class_id.objects.filter(teacher=teacher_id).order_by('name')
    return render(request, 'custom_users/ajax_load_classes.html', {'class_ids': class_ids})
