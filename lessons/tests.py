from django.test import Client, TestCase
from django.urls import reverse
from exams.models import Level
from .models import Lesson


class LessonsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Level.objects.create(title = "1")
        level = Level.objects.get(id=1)
        Lesson.objects.create(level = level, title = "test_lesson_1", link = "www.testlink1.com", number = 1)

    def setUp(self):
        self.lesson = Lesson.objects.get(id=1)
        self.client = Client()
    # models tests
    def test_str(self):
        self.assertEquals(self.lesson.__str__(), "test_lesson_1")

    # views tests
    def test_complete_lesson_response(self):
        response = self.client.get(reverse('complete_lesson', args=[1,]))
        self.assertEquals(response.status_code, 200)

    def test_complete_lesson_template(self):
        response = self.client.get(reverse('complete_lesson', args=[1,]))
        self.assertTemplateUsed(response, 'lessons/view_lesson.html')

    def test_complete_lesson_html(self):
        response = self.client.get(reverse('complete_lesson', args=[1,]))
        self.assertContains(response, "<h5>Lesson Title: test_lesson_1</h5>")
