from custom_users.models import StudentProfile
from exams.utils import get_next_lesson
from .models import Lesson

"""
Function to add a lesson to a student's completed lesson list
and get the lesson.id for the student's next lesson
"""
def add_lesson_completed(user_id):
    student = StudentProfile.objects.get(user_id = user_id)
    try:
        lesson = Lesson.objects.get(id = student.next_lesson_id)
        student.completed_lessons.add(lesson)
        get_next_lesson(student.user_id)
    except Lesson.DoesNotExist:
        pass