from django.shortcuts import render
from users.models import Class_id, StudentProfile, User

def class_list(request, user_id):
    if User.objects.get(id = user_id).is_teacher:
        user = User.objects.get(id = user_id)
        classes = Class_id.objects.all().filter(teacher = user_id)
        return render(request, 'teachers/class_list.html', {
        'user': user,
        'classes':classes,
        'teacher':user
        })
    else:
        return render(request, 'teachers/not_teacher.html')

def show_students(request, class_name, teacher_id):
    group = Class_id.objects.get(name = class_name, teacher = teacher_id)
    students = StudentProfile.objects.all().filter(class_id = group.id)
    return render(request, 'teachers/show_students.html', {
    'group': group,
    'students': students,
    })
