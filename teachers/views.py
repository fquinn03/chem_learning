from django.shortcuts import render
from users.models import Class_id, User
from users.views import show_students

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
