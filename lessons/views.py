from django.shortcuts import render
from .models import Lesson

"""
View to display a lesson object.
Lesson objects can be Microsoft office powerpoints,
youtube videos or similar (referenced by embed link)
"""
def complete_lesson(request, lesson_id):
    lesson = Lesson.objects.get(id = lesson_id)
    return render(request, 'lessons/view_lesson.html', {
    'lesson': lesson,
    })
