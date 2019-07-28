from django.test import TestCase, Client
from django.urls import reverse
from users.models import User

class TeacherTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(id = 1, username ="teacher", is_student = False, is_teacher = True)
        User.objects.create(id = 2, username ="student", is_student = True, is_teacher = False)

    def setUp(self):
        self.client = Client()
        self.teacher = User.objects.get(id=1)
        self.student = User.objects.get(id=2)

    def test_is_teacher(self):
        self.assertEquals(self.teacher.is_teacher, True)

    def test_is_not_teacher(self):
        self.assertEquals(self.teacher.is_student, False)

    def test_is_not_student(self):
        self.assertEquals(self.student.is_teacher, False)

    def test_is_student(self):
        self.assertEquals(self.student.is_student, True)

    def test_class_list_teacher_response(self):
        response = self.client.get(reverse('class_list', args=[1] ))
        self.assertEquals(response.status_code, 200)

    def test_class_list_teacher_template(self):
        response = self.client.get(reverse('class_list', args=[1] ))
        self.assertTemplateUsed(response, "teachers/class_list.html")

    def test_class_list_teacher_html(self):
        response = self.client.get(reverse('class_list', args=[1] ))
        self.assertContains(response, "<h1>Welcome teacher </h1>")

    def test_class_list_student_response(self):
        response = self.client.get(reverse('class_list', args=[2] ))
        self.assertEquals(response.status_code, 200)

    def test_class_list_student_template(self):
        response = self.client.get(reverse('class_list', args=[2] ))
        self.assertTemplateUsed(response, "teachers/not_teacher.html")

    def test_class_list_student_html(self):
        response = self.client.get(reverse('class_list', args=[2] ))
        self.assertContains(response, "<p>You do teach any classes</p>")
