from django.contrib.auth.decorators import user_passes_test, login_required
from custom_users.utils import user_is_teacher, user_is_student
from custom_users.models import StudentProfile
from django.shortcuts import render, redirect
from exams.utils import get_next_lesson
from .models import Lesson
from .utils import add_lesson_completed

"""
Check the user is a student
Display a lesson object for student.
Lesson objects can be Microsoft office powerpoints,
youtube videos or similar (referenced by embed link)
"""
@login_required
@user_passes_test(user_is_student, login_url = 'welcome_teacher')
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
Check the user is a student
Leave the current lesson and move on to the next lesson
"""
@login_required
@user_passes_test(user_is_student, login_url = 'welcome_teacher')
def mark_lesson_as_complete(request):
    add_lesson_completed(request.user.id)
    return redirect('complete_lesson')

"""
Leave the current lesson and move on to the next quiz
"""
@login_required
@user_passes_test(user_is_student, login_url = 'welcome_teacher')
def take_the_next_quiz(request):
    add_lesson_completed(request.user.id)
    return redirect('dotest')

"""
Check the user is a student
Leave the current lesson and go back to the student welcome screen
"""
@login_required
@user_passes_test(user_is_student, login_url = 'welcome_teacher')
def go_back_to_welcome_student(request):
    add_lesson_completed(request.user.id)
    return redirect('welcome_student')
