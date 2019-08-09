from django.test import Client, TestCase
from django.urls import reverse
from custom_users.models import User
from exams.models import Level
from .models import Lesson

"""
Unit tests for all of the lessons views.
NOTE: force_login method is used instead of login() when a test requires a user be logged in
and the details of how a user logged in aren’t important.
This method is faster than login() since the expensive password hashing algorithms are bypassed
"""

class LessonsTest(TestCase):
    @classmethod
    # set up test database
    def setUpTestData(cls):
        User.objects.create(id = 2, username = "student1", password="student1_pass")
        Level.objects.create(title = "1")
        level = Level.objects.get(id=1)
        Lesson.objects.create(level = level, title = "test_lesson_1", link = "www.testlink1.com", number = 1)

    def setUp(self):
    # set up Lessons TestCase
        self.lesson = Lesson.objects.get(id=1)
        self.client = Client()

    """
    Models Tests
    """
    # test str method
    def test_str(self):
        self.assertEqual(self.lesson.__str__(), "test_lesson_1")

    """
    Views and Template testing

    Each view is tested for expected response using
    assertEqual(response.status_code, )
    using GET requests (and POST requests where relevant).

    Template rendered is tested using assertTemplateUsed()
    This checks the correct template is rendered for logged in
    user type and the type of request.

    The template and context are tested using assertContains(), to
    ensure the correct template has been rendered with the correct
    context data for logged in user where relevant.

    """
    # test complete_lesson view
    def test_complete_lesson_response(self):
        self.client.force_login(User.objects.get(id=2))
        response = self.client.get(reverse('complete_lesson', args=[1,]))
        self.assertEqual(response.status_code, 200)

    def test_complete_lesson_template(self):
        self.client.force_login(User.objects.get(id=2))
        response = self.client.get(reverse('complete_lesson', args=[1,]))
        self.assertTemplateUsed(response, 'lessons/view_lesson.html')

    def test_complete_lesson_html(self):
        self.client.force_login(User.objects.get(id=2))
        response = self.client.get(reverse('complete_lesson', args=[1,]))
        self.assertContains(response, "<h5>Lesson Title: test_lesson_1</h5>")
