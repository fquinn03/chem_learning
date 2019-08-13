from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from custom_users.models import (Class_id, TeacherProfile,
School, StudentProfile)
from lessons.models import Lesson

"""
Unit tests for all of the teachers views.
NOTE: force_login method is used instead of login() when a test requires a user be logged in
and the details of how a user logged in aren’t important.
This method is faster than login() since the expensive password hashing algorithms are bypassed
"""

class TeacherTest(TestCase):

    @classmethod
    # set up test database
    def setUpTestData(cls):
        Lesson.objects.create(level = 1, title = "test_lesson",
        link = "a_doc_link", image_link = "an_image_link")
        User.objects.create_user(username ="teacher", password="mypass")
        User.objects.create_user(username ="student1", password="mypass")
        Class_id.objects.create(name = "9y3", teacher_id = 1)
        School.objects.create(name = "test_school", post_code = "testpostcode")
        school = School.objects.get(id = 1)
        teacher = User.objects.get(id=1)
        student = User.objects.get(id=2)
        class_id = Class_id.objects.get(id=1)
        TeacherProfile.objects.create(user = teacher, is_teacher = True,
        is_student = False, school = school, details_added = True )
        teacherprofile = TeacherProfile.objects.get(user_id=1)
        StudentProfile.objects.create(user = student, teacher = teacherprofile,
        class_id = class_id, details_added = True, signup_quiz_completed = True,
        next_lesson_id = 1 )

    def setUp(self):
        #set up TeacerTest TestCase
        self.teacher = User.objects.get(id=1)
        self.student = User.objects.get(id=2)
        self.teacherprofile = TeacherProfile.objects.get(user_id = 1)
        self.studentprofile = StudentProfile.objects.get(user_id = 2)
        self.class1 = Class_id.objects.get(id=1)
        self.client = Client()

    """
    Models Tests
    """
    #test flags when TeacherProfile object created
    def test_is_teacher(self):
        self.assertEqual(self.teacherprofile.is_teacher, True)

    def test_teacher_is_student(self):
        self.assertEqual(self.teacherprofile.is_student, False)

    def test_is_student(self):
        self.assertEqual(self.studentprofile.is_student, True)

    def test_student_is_teacher(self):
        self.assertEqual(self.studentprofile.is_teacher, False)

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

    # test show_students view
    def test_show_students_response(self):
        self.client.login(username = "teacher", password = "mypass")
        response = self.client.get(reverse('show_students', args=['9y3']))
        self.assertEqual(response.status_code, 200)

    def test_show_students_template(self):
        self.client.login(username = "teacher", password = "mypass")
        response = self.client.get(reverse('show_students', args=['9y3']))
        self.assertTemplateUsed(response, "teachers/show_students.html")

    def test_show_students_html(self):
        self.client.login(username = "teacher", password = "mypass")
        response = self.client.get(reverse('show_students', args=['9y3']))
        self.assertContains(response, "<th>Student</th>")

    # test class_list view. Logged in as Teacher and Student
    def test_class_list_teacher_response(self):
        self.client.login(username = "teacher", password = "mypass")
        response = self.client.get(reverse('class_list'))
        self.assertEqual(response.status_code, 200)

    def test_class_list_teacher_template(self):
        self.client.login(username = "teacher", password = "mypass")
        response = self.client.get(reverse('class_list'))
        self.assertTemplateUsed(response, "teachers/class_list.html")

    def test_class_list_teacher_html(self):
        self.client.login(username = "teacher", password = "mypass")
        response = self.client.get(reverse('class_list' ))
        self.assertContains(response, "<h5>Welcome teacher </h5>")

    def test_class_list_student_response(self):
        self.client.login(username = "student1", password = "mypass")
        response = self.client.get(reverse('class_list'))
        self.assertTrue(response.status_code, 302)

    def test_class_list_student_template(self):
        self.client.login(username = "student1", password = "mypass")
        response = self.client.get(reverse('class_list'), follow = True)
        self.assertTemplateUsed(response, "custom_users/welcome_student.html")

    def test_class_list_student_html(self):
        self.client.login(username = "student1", password = "mypass")
        response = self.client.get(reverse('class_list'), follow = True)
        self.assertContains(response, "<h5><strong>Welcome Student:</strong> student1</h5>")
