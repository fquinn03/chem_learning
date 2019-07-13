from django.urls import reverse
from django.test import TestCase, Client
from users.models import User, Class_id, StudentProfile, TeacherProfile



class UserTest(TestCase):
    def setUp(cls):
        User.objects.create(id = 1, username ="teacher", is_student = False, is_teacher = True)
        User.objects.create(id = 2, username ="student", is_student = True, is_teacher = False)
        Class_id.objects.create(id = 1, name = "9y3", teacher_id = 1)
        teacher = User.objects.get(id=1)
        student = User.objects.get(id=2)
        class_id = Class_id.objects.get(id=1)
        TeacherProfile.objects.create()
        teacherprofile = TeacherProfile.objects.get(user_id=1)
        StudentProfile.objects.create(user = student, teacher = teacherprofile, class_id = class_id)

    def test_is_teacher(self):
        teacher = User.objects.get(id=1)
        student = User.objects.get(id=2)
        self.assertEquals(teacher.is_teacher, True)
        self.assertEquals(teacher.is_student, False)
        self.assertEquals(student.is_teacher, False)
        self.assertEquals(student.is_student, True)

    def test_studentProfile(self):
        sp = StudentProfile.objects.get(user_id=2)
        self.assertEquals(sp.class_id.name, "9y3")

    def test_TeacherProfile_as_string(self):
        tp = TeacherProfile.objects.get(user_id = 1)
        self.assertEquals(tp.__str__(), "teacher")

    def test_studentProfile_as_string(self):
        sp = StudentProfile.objects.get(user_id = 2)
        self.assertEquals(sp.__str__(), "student")

    def test_class_id_as_string(self):
        class1 = Class_id.objects.get(id=1)
        self.assertEquals(class1.__str__(), "9y3")

    def test_show_students(self):
        client = Client()
        response = client.get(reverse('show_students', args=['9y3']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/show_students.html")
