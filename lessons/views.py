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
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.get(user_id = request.user.id)
            lesson = Lesson.objects.get(id = lesson_id)
            if student.details_added and student.signup_quiz_completed:
                if student.next_lesson_id == lesson.id:
                    return render(request, 'lessons/view_lesson.html', {
                    'lesson': lesson,
                    })
                else:
                    return redirect('welcome_student')
            elif student.student_details_added:
                return redirect('do_signup_quiz')
            else:
                return redirect('edit_student')
        except:
            return redirect('home')
    else:
        return redirect('signup')
