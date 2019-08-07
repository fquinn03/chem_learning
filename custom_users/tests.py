from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from .models import  Class_id, School, StudentProfile, TeacherProfile, User
from .forms import StudentProfileForm
from .views import edit_student

class UserTest(TestCase):
    # set up testing database
    @classmethod
    def setUpTestData(cls):
        School.objects.create(id = 1, name = "Freedom Highschool", post_code = "AB1 2CD")
        User.objects.create(id = 1, username = "teacher", password="teacher_pass")
        User.objects.create(id = 2, username = "student1", password="student1_pass")
        User.objects.create(id = 3, username = "student2", password="student2_pass")
        Class_id.objects.create(id = 1, name = "9y3", teacher_id=1)
        teacher = User.objects.get(id = 1)
        student = User.objects.get(id = 2)
        another_student = User.objects.get(id=3)
        school = School.objects.get(id =1)
        class_id=Class_id.objects.get(id = 1)
        TeacherProfile.objects.create(user_id = 1, school_id = school.id)
        teacherprofile=TeacherProfile.objects.get(user_id = 1)
        StudentProfile.objects.create(user=student, teacher=teacherprofile, class_id = class_id, school_id = school.id)
        StudentProfile.objects.create(user=another_student, teacher=teacherprofile, class_id = class_id, school_id = school.id)
    def setUp(self):
        # set up TestCase
        self.client=Client()
        self.teacher=User.objects.get(id = 1)
        self.student=User.objects.get(id = 2)
        self.tp=TeacherProfile.objects.get(user_id = 1)
        self.sp=StudentProfile.objects.get(user_id = 2)
        self.class1=Class_id.objects.get(id = 1)
        self.user=User.objects.get(id = 3)
        self.school = School.objects.get(id=1)
        self.class_id = Class_id.objects.get(id=1)


    # models tests
    #test isteacher, isstudent on UserModel
    def test_user_model_userid(self):
        self.assertEqual(self.user.id, 3)

    def test_user_model_username(self):
        self.assertEqual(self.user.username, "student2")

    def test_user_model_password(self):
        self.assertEqual(self.user.password, "student2_pass")

    def test_is_teacher(self):
        self.assertEqual(self.tp.is_teacher, True)

    def test_is_student(self):
        self.assertEqual(self.sp.is_student, True)

    # test __str__methods
    def test_studentProfile(self):
        self.assertEqual(self.sp.class_id.name, "9y3")

    def test_TeacherProfile_as_string(self):
        self.assertEqual(self.tp.__str__(), "teacher")

    def test_studentProfile_as_string(self):
        self.assertEqual(self.sp.__str__(), "student1")

    def test_class_id_as_string(self):
        self.assertEqual(self.class1.__str__(), "9y3")

    # views tests
    def test_welcome_student_response(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('welcome_student'))
        self.assertEqual(response.status_code, 200)

    def test_welcome_student_template(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('welcome_student'))
        self.assertTemplateUsed(response, "custom_users/welcome_student.html")

    def test_welcome_student_html(self):
        """
        Use this method instead of login() when a test requires a user be logged in and the details of how a user logged in aren’t important.
        This method is faster than login() since the expensive password hashing algorithms are bypassed
        """
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('welcome_student'))
        self.assertContains(response, "<h5>Welcome Student: student1</h5>")

    def test_welcome_teacher_response(self):
        response=self.client.get(reverse('welcome_teacher'))
        self.assertEqual(response.status_code, 200)

    def test_welcome_teacher_template(self):
        response=self.client.get(reverse('welcome_teacher'))
        self.assertTemplateUsed(response, "custom_users/welcome_teacher.html")

    def test_welcome_teacher_html(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('welcome_teacher'))
        self.assertContains(response, "<h5>Welcome Teacher: teacher</h5>")

    def test_edit_student_get(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('edit_student'))
        self.assertEqual(response.status_code, 200)

    def test_edit_student_post(self):
        request_param = {'school':['1'], 'teacher':['1'], 'class_id':['1']}
        rf = RequestFactory()
        url = reverse('edit_student')
        request = rf.get(url, request_param )
        request.user = self.user
        response = edit_student(request)
        self.assertEqual(response.status_code, 200)

    def test_form_not_valid(self):
        form = StudentProfileForm()
        self.assertEqual(form.is_valid(), False)

    def test_form_valid(self):
        student = self.sp
        form = StudentProfileForm({'school': "", 'teacher': "",'class_id': ""}, instance = student)
        self.assertEqual(form.is_valid(), True)

    def test_form_valid_with_data(self):
        school_id = 1
        student = self.sp
        form = StudentProfileForm({'school': 1, 'teacher': "",'class_id': ""}, instance = student)
        self.assertEqual(form.fields['teacher'].queryset[0], TeacherProfile.objects.get(school_id = school_id))

    def test_form_valid_with_more_data(self):
        school_id = 1
        teacher_id = 1
        student = self.sp
        form = StudentProfileForm({'school': 1, 'teacher': 1,'class_id': ""}, instance = student)
        self.assertEqual(form.fields['class_id'].queryset[0], Class_id.objects.get(teacher_id = teacher_id))
