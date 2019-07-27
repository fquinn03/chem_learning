from django.test import TestCase, Client
from django.urls import reverse
from .models import Lesson
from exams.models import Level

class LessonsTest(TestCase):
    def setUp(cls):
        Level.objects.create(title = "1")
        level = Level.objects.get(id=1)
        Lesson.objects.create(level = level, title = "test_lesson_1", link = "www.testlink1.com", number = 1)

    # models tests
    def test_str(self):
        lesson = Lesson.objects.get(id=1)
        self.assertEquals(lesson.__str__(), "test_lesson_1")

    # views tests
    def test_complete_lesson(self):
        lesson = Lesson.objects.get(id=1)
        client = Client()
        response = client.get(reverse('complete_lesson', args=[1,]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/view_lesson.html')
