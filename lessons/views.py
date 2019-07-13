from django.shortcuts import render
from .models import Lesson

def complete_lesson(request, lesson_id):
    lesson = Lesson.objects.get(id = lesson_id)
    return render(request, 'lessons/view_lesson.html', {
    'lesson': lesson,
    })
