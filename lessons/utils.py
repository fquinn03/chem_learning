from custom_users.models import StudentProfile
from exams.utils import get_next_lesson
from .models import Lesson

def add_lesson_completed(request):
    student = StudentProfile.objects.get(user_id = request.user.id)
    lesson = Lesson.objects.get(id = student.next_lesson_id)
    student.completed_lessons.add(lesson)
    get_next_lesson(student.user_id)
