from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from custom_users.models import Class_id, TeacherProfile, StudentProfile

class TeacherTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username ="teacher", password="mypass")
        User.objects.create(username ="student1", password="mypass")
        Class_id.objects.create(id = 1, name = "9y3", teacher_id = 1)
        teacher = User.objects.get(id=1)
        student = User.objects.get(id=2)
        class_id = Class_id.objects.get(id=1)
        TeacherProfile.objects.create(user_id=1)
        teacherprofile = TeacherProfile.objects.get(user_id=1)
        StudentProfile.objects.create(user = student, teacher = teacherprofile, class_id = class_id)

    def setUp(self):
        self.client = Client()
        self.teacher = User.objects.get(id=1)
        self.student = User.objects.get(id=2)
        self.teacherprofile = TeacherProfile.objects.get(user_id = 1)
        self.studentprofile = StudentProfile.objects.get(user_id = 2)
        self.class1 = Class_id.objects.get(id=1)

    def test_is_teacher(self):
        self.assertEquals(self.teacherprofile .is_teacher, True)

    def test_is_student(self):
        self.assertEquals(self.studentprofile.is_student, True)

    def test_show_students_response(self):
        response = self.client.get(reverse('show_students', args=['9y3', 1]))
        self.assertEquals(response.status_code, 200)

    def test_show_students_template(self):
        response = self.client.get(reverse('show_students', args=['9y3', 1]))
        self.assertTemplateUsed(response, "teachers/show_students.html")
        """
    def test_show_students_html(self):
        self.client.force_login(User.objects.get(id=2))
        response = self.client.get(reverse('show_students', args=['9y3', 1]))
        self.assertContains(response, "<td>student</td>")
        """
    def test_class_list_teacher_response(self):
        response = self.client.get(reverse('class_list', args=[1] ))
        self.assertEquals(response.status_code, 200)

    def test_class_list_teacher_template(self):
        response = self.client.get(reverse('class_list', args=[1] ))
        self.assertTemplateUsed(response, "teachers/class_list.html")
        """
    def test_class_list_teacher_html(self):
        self.client.force_login(User.objects.get(id=1))
        response = self.client.get(reverse('class_list', args=[1] ))
        self.assertContains(response, "<h5>Welcome teacher </h5>")
        """
    def test_class_list_student_response(self):
        response = self.client.get(reverse('class_list', args=[1] ))
        self.assertTrue(response.status_code, 200)

    def test_class_list_student_template(self):
        response = self.client.get(reverse('class_list', args=[1] ))
        self.assertTemplateUsed(response, "teachers/not_teacher.html")

    def test_class_list_student_html(self):
        response = self.client.get(reverse('class_list', args=[2] ))
        self.assertContains(response, "<p>You do teach any classes</p>")
