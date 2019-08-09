from django.contrib.auth.models import User
from django.shortcuts import render
from custom_users.models import Class_id, StudentProfile, TeacherProfile

"""
If user is a teacher, a list of their classes is sent to the template
If not they are redirected to not teacher template
"""
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

"""
If a teacher clicks on a class in the above class_list view/template
A list of students in that class is sent to the template.
"""
def show_students(request, class_name):
    user = request.user
    teacher = TeacherProfile.objects.get(user_id = user.id)
    group = Class_id.objects.get(name = class_name, teacher_id = user.id)
    students = StudentProfile.objects.filter(class_id = group.id)
    return render(request, 'teachers/show_students.html', {
    'group': group,
    'students': students,
    })
