from django.contrib.auth.decorators import user_passes_test, login_required
from custom_users.utils import user_is_teacher, user_is_student
from django.shortcuts import render, redirect
from custom_users.models import StudentProfile
from .models import Lesson


"""
View to display a lesson object.
Lesson objects can be Microsoft office powerpoints,
youtube videos or similar (referenced by embed link)
"""
@login_required
@user_passes_test(user_is_student)
def complete_lesson(request, lesson_id):
    student = StudentProfile.objects.get(user_id = request.user.id)
    lesson = Lesson.objects.get(id = lesson_id)
    return render(request, 'lessons/view_lesson.html', {
    'lesson': lesson,
    })
