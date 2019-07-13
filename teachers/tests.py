from django.test import TestCase, Client
from django.urls import reverse
from users.models import User

class TeacherTest(TestCase):
    def setUp(cls):
        User.objects.create(id = 1, username ="teacher", is_student = False, is_teacher = True)
        User.objects.create(id = 2, username ="student", is_student = True, is_teacher = False)

    def test_class_list_teacher(self):
        teacher = User.objects.get(id=1)
        student = User.objects.get(id=2)
        client = Client()
        response = client.get(reverse('class_list', args=[1] ))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "teachers/class_list.html")

    def test_class_list_student(self):
        teacher = User.objects.get(id=1)
        student = User.objects.get(id=2)
        client = Client()
        response = client.get(reverse('class_list', args=[2] ))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "teachers/not_teacher.html")
