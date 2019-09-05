from django.contrib.auth.decorators import user_passes_test, login_required
from custom_users.utils import user_is_teacher, user_is_student
from custom_users.models import StudentProfile
from django.shortcuts import render, redirect
from exams.utils import get_next_lesson
from .models import Lesson
from .utils import add_lesson_completed

"""
View to display a lesson object.
Lesson objects can be Microsoft office powerpoints,
youtube videos or similar (referenced by embed link)
"""
@login_required
@user_passes_test(user_is_student)
def complete_lesson(request):
    student = StudentProfile.objects.get(user_id = request.user.id)
    try:
        lesson = Lesson.objects.get(id = student.next_lesson_id)
        return render(request, 'lessons/view_lesson.html', {
        'lesson': lesson,
        })
    except Lesson.DoesNotExist:
        return redirect('congratulations')

"""
View to move from view_lesson.html on to the next lesson
"""
@login_required
@user_passes_test(user_is_student)
def mark_lesson_as_complete(request):
    try:
        add_lesson_completed(request.user.id)
        return redirect('complete_lesson')
    except IndexError:
        return redirect('congratulations')

"""
View to move from view_lesson.html on to the next quiz
"""
@login_required
@user_passes_test(user_is_student)
def take_the_next_quiz(request):
    add_lesson_completed(request.user.id)
    return redirect('dotest')

"""
View to move from view_lesson.html back to the welcome screen
"""
@login_required
@user_passes_test(user_is_student)
def go_back_to_welcome_student(request):
    add_lesson_completed(request.user.id)
    return redirect('welcome_student')
