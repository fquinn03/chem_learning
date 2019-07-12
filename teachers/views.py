from django.shortcuts import render
from users.models import Class_id
from users.models import User


def class_list(request, user_id):
    if User.objects.get(id = user_id).is_teacher:
        users = User.objects.all().filter(id = user_id)
        classes = Class_id.objects.all().filter(teacher = user_id)
        return render(request, 'teachers/class_list.html', {
        'users': users,
        'classes':classes,
        })
    else:
        return render(request, 'teachers/not_teacher.html')
