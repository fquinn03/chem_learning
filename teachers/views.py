from django.contrib.auth.models import User
from django.shortcuts import render
from custom_users.models import Class_id, StudentProfile, TeacherProfile


def class_list(request):
    user = request.user
    try:
        teacher = TeacherProfile.objects.get(user_id = user.id)
        if teacher:
            classes = Class_id.objects.filter(teacher = teacher)
            return render(request, 'teachers/class_list.html', {
            'user': user,
            'classes':classes,
            })
    except:
        return render(request, 'teachers/not_teacher.html')

def show_students(request, class_name):
    user = request.user
    teacher = TeacherProfile.objects.get(user_id = user.id)
    group = Class_id.objects.get(name = class_name, teacher_id = user.id)
    students = StudentProfile.objects.filter(class_id = group.id)
    return render(request, 'teachers/show_students.html', {
    'group': group,
    'students': students,
    })
