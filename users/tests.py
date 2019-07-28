from django.urls import reverse
from django.test import Client, TestCase
from users.models import  Class_id, StudentProfile, TeacherProfile, User

class UserTest(TestCase):
    # set up testing database
    @classmethod
    def setUpTestData(cls):
        User.objects.create(id = 1, username ="teacher", is_student = False, is_teacher = True)
        User.objects.create(id = 2, username ="student", is_student = True, is_teacher = False)
        Class_id.objects.create(id = 1, name = "9y3", teacher_id = 1)
        teacher = User.objects.get(id=1)
        student = User.objects.get(id=2)
        class_id = Class_id.objects.get(id=1)
        TeacherProfile.objects.create()
        teacherprofile = TeacherProfile.objects.get(user_id=1)
        StudentProfile.objects.create(user = student, teacher = teacherprofile, class_id = class_id)

    def setUp(self):
        # set up TestCase
        self.client = Client()
        self.teacher = User.objects.get(id=1)
        self.student = User.objects.get(id=2)
        self.tp = TeacherProfile.objects.get(user_id = 1)
        self.sp = StudentProfile.objects.get(user_id=2)
        self.class1 = Class_id.objects.get(id=1)
    # models tests
    #test isteacher, isstudent on UserModel
    def test_is_teacher(self):
        self.assertEquals(self.teacher.is_teacher, True)

    def test_is_not_teacher(self):
        self.assertEquals(self.teacher.is_student, False)

    def test_is_not_student(self):
        self.assertEquals(self.student.is_teacher, False)

    def test_is_student(self):
        self.assertEquals(self.student.is_student, True)

    # test __str__methods
    def test_studentProfile(self):
        self.assertEquals(self.sp.class_id.name, "9y3")

    def test_TeacherProfile_as_string(self):
        self.assertEquals(self.tp.__str__(), "teacher")

    def test_studentProfile_as_string(self):
        self.assertEquals(self.sp.__str__(), "student")

    def test_class_id_as_string(self):
        self.assertEquals(self.class1.__str__(), "9y3 teacher")

    # views tests
    def test_show_students_response(self):
        response = self.client.get(reverse('show_students', args=['9y3', 1]))
        self.assertEquals(response.status_code, 200)

    def test_show_students_template(self):
        response = self.client.get(reverse('show_students', args=['9y3', 1]))
        self.assertTemplateUsed(response, "users/show_students.html")

    def test_show_students_html(self):
        response = self.client.get(reverse('show_students', args=['9y3', 1]))
        self.assertContains(response, "<td>student</td>")

    def test_welcome_response(self):
        response = self.client.get(reverse('welcome'))
        self.assertEquals(response.status_code, 200)

    def test_welcome_template(self):
        response = self.client.get(reverse('welcome'))
        self.assertTemplateUsed(response, "users/welcome.html")

    def test_welcome_html(self):
        response = self.client.get(reverse('welcome'))
        self.assertContains(response, "<p>Learn how to write chemical equations</p>")
