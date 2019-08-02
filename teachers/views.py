from django.shortcuts import render
from custom_users.models import Class_id, StudentProfile, TeacherProfile


def class_list(request, user_id):
    try:
        teacher = TeacherProfile.objects.get(user_id = user_id)
        if teacher:
            classes = Class_id.objects.all().filter(teacher = teacher)
            return render(request, 'teachers/class_list.html', {
            'teacher': teacher,
            'classes': classes,
        })
    except:
        return render(request, 'teachers/not_teacher.html')

def show_students(request, class_name, user_id):
    teacher = TeacherProfile.objects.get(user_id = user_id)
    group = Class_id.objects.get(name = class_name, teacher = teacher)
    students = StudentProfile.objects.all().filter(class_id = group.id)
    return render(request, 'teachers/show_students.html', {
    'group': group,
    'students': students,
    })
