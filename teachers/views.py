from django.shortcuts import render
from users.models import Class_id


def class_list(request, user_id):
    classes = Class_id.objects.all().filter(teacher = user_id)
    return render(request, 'teachers/class_list.html', {
    'classes':classes,
    })
