from django.shortcuts import render
from users.models import Class_id
from users.models import User


def class_list(request, user_id):
    if User.objects.get(id = user_id).is_teacher:
        user = User.objects.get(id = user_id)
        classes = Class_id.objects.all().filter(teacher = user_id)
        return render(request, 'teachers/class_list.html', {
        'user': user,
        'classes':classes,
        })
    else:
        return render(request, 'teachers/not_teacher.html')


def show_students(request, teacher_id, class_name):
    Class_id = Class_id.objects.all().filter(teacher = teacher_id, name = class_name)
    return render(request, 'teachers/show_students.html',{
    'class_id':class_id
    })
