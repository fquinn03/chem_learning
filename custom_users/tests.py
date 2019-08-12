from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from lessons.models import Lesson
from .models import  Class_id, School, StudentProfile, TeacherProfile, User
from .forms import StudentProfileForm
from .views import edit_student, signup_form_student, signup_form_teacher

"""
Unit tests for all of the custom_users views and forms.
NOTE: force_login method is used instead of login() when a test requires a user be logged in
and the details of how a user logged in aren’t important.
This method is faster than login() since the expensive password hashing algorithms are bypassed
"""

class CustomUsersTest(TestCase):
    # set up test database
    @classmethod
    def setUpTestData(cls):
        School.objects.create(id = 1, name = "Freedom Highschool", post_code = "AB1 2CD")
        School.objects.create(id = 2, name = "SomeSchool", post_code = "SomePostCode")
        User.objects.create(id = 1, username = "teacher", password="teacher_pass")
        User.objects.create(id = 2, username = "student1", password="student1_pass")
        User.objects.create(id = 3, username = "student2", password="student2_pass")
        User.objects.create(id = 4, username = "student3", password="student3_pass")
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
        Lesson.objects.create(level = 1, title = "test_lesson_1_1", link = "www.testlink1.com")

    def setUp(self):
        # set up CustomUsers TestCase
        self.client=Client()
        self.teacher=User.objects.get(id = 1)
        self.student=User.objects.get(id = 2)
        self.tp=TeacherProfile.objects.get(user_id = 1)
        self.sp=StudentProfile.objects.get(user_id = 2)
        self.class1=Class_id.objects.get(id = 1)
        self.user=User.objects.get(id = 3)
        self.school = School.objects.get(id=1)
        self.class_id = Class_id.objects.get(id=1)
        self.user3 = User.objects.get(id = 4)


    """
    Models Tests
    """
    # Test basic User model queries are returning expected data
    def test_user_model_userid(self):
        self.assertEqual(self.user.id, 3)

    def test_user_model_username(self):
        self.assertEqual(self.user.username, "student2")

    def test_user_model_password(self):
        self.assertEqual(self.user.password, "student2_pass")

    # Test default setup flags are working as expected
    def test_is_teacher(self):
        self.assertEqual(self.tp.is_teacher, True)

    def test_teacher_is_student(self):
        self.assertEqual(self.tp.is_student, False)

    def test_is_student(self):
        self.assertEqual(self.sp.is_student, True)

    def test_student_is_teacher(self):
        self.assertEqual(self.sp.is_teacher, False)

    # test __str__methods
    def test_studentProfile(self):
        self.assertEqual(self.sp.class_id.name, "9y3")

    def test_TeacherProfile_as_string(self):
        self.assertEqual(self.tp.__str__(), "teacher")

    def test_studentProfile_as_string(self):
        self.assertEqual(self.sp.__str__(), "student1")

    def test_class_id_as_string(self):
        self.assertEqual(self.class1.__str__(), "9y3")

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
    Additional testing for individual views is added and explained
    where necessary.
    """

    # test welcome student view
    def test_welcome_student_response(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('welcome_student'))
        self.assertEqual(response.status_code, 200)

    def test_welcome_student_template(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('welcome_student'))
        self.assertTemplateUsed(response, "custom_users/welcome_student.html")

    def test_welcome_student_html(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('welcome_student'))
        self.assertContains(response, "<h5><strong>Welcome Student:</strong> student1</h5>")

    # test welcome teacher view
    def test_welcome_teacher_response(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('welcome_teacher'))
        self.assertEqual(response.status_code, 200)

    def test_welcome_teacher_template(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('welcome_teacher'))
        self.assertTemplateUsed(response, "custom_users/welcome_teacher.html")

    def test_welcome_teacher_html(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('welcome_teacher'))
        self.assertContains(response, "<h5>Welcome Teacher: teacher</h5>")

    # test the StudentProfile form with valid and invalid data
    def test_form_not_valid(self):
        form = StudentProfileForm()
        self.assertEqual(form.is_valid(), False)

    def test_form_valid(self):
        student = self.sp
        form = StudentProfileForm({'school': "", 'teacher': "",'class_id': ""}, instance = student)
        self.assertEqual(form.is_valid(), True)

    # check that the dropdown will have the correct data when a school is selected
    def test_form_valid_with_data(self):
        school_id = 1
        student = self.sp
        form = StudentProfileForm({'school': 1, 'teacher': "",'class_id': ""}, instance = student)
        self.assertEqual(form.fields['teacher'].queryset[0], TeacherProfile.objects.get(school_id = school_id))

    # check that the dropdown will have the correct data when a class is selected
    def test_form_valid_with_more_data(self):
        school_id = 1
        teacher_id = 1
        student = self.sp
        form = StudentProfileForm({'school': 1, 'teacher': 1,'class_id': ""}, instance = student)
        self.assertEqual(form.fields['class_id'].queryset[0], Class_id.objects.get(teacher_id = teacher_id))

    #tests for signup view
    def test_signup_response(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_html(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, '<h3>Sign up for a free account</h3>')

    #test for signup_form_student view, GET and POST requests
    def test_sign_up_form_student_get_response(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('signup_form_student'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_form_student_get_template(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('signup_form_student'))
        self.assertTemplateUsed(response, "signup_form_student.html")

    def test_sign_up_form_student_get_html(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('signup_form_student'))
        self.assertContains(response,'<div class="card-headergreen">Student sign up</div>')

    def test_sign_up_form_student_post_response(self):
        response=self.client.post(reverse('signup_form_student'),
        {'username': 'student5', 'password1': 'pass1234', 'password2': 'pass1234'}, follow = True)
        self.assertEqual(response.status_code, 200)

    # check that when a new user signs up, a new User is added to the database
    def test_sign_up_form_student_post_count_users(self):
        count = User.objects.all().count()
        response=self.client.post(reverse('signup_form_student'),
        {'username': 'student5', 'password1': 'pass1234', 'password2': 'pass1234'})
        count2 = User.objects.all().count()
        self.assertEqual(count2, count+1)

    # check that when a new studentuser signs up a new StudentProfile is added to the database
    def test_sign_up_form_student_post_count_students(self):
        count = StudentProfile.objects.all().count()
        response=self.client.post(reverse('signup_form_student'),
        {'username': 'student5', 'password1': 'pass1234', 'password2': 'pass1234'})
        count2 = StudentProfile.objects.all().count()
        self.assertEqual(count2, count+1)

    def test_sign_up_form_student_post_template(self):
        response=self.client.post(reverse('signup_form_student'),
        {'username': 'student5', 'password1': 'pass1234', 'password2': 'pass1234'}, follow = True)
        self.assertTemplateUsed(response, 'custom_users/edit_student.html')

    def test_sign_up_form_student_post_html(self):
        response=self.client.post(reverse('signup_form_student'),
        {'username': 'student5', 'password1': 'pass1234', 'password2': 'pass1234'}, follow = True)
        self.assertContains(response, '<div class="card-headergreen">Add Student Details</div>')

    # test signup_form_teacher views. GET and POST requests.
    def test_sign_up_form_teacher_get_response(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('signup_form_teacher'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_form_teacher_get_template(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('signup_form_teacher'))
        self.assertTemplateUsed(response, "signup_form_teacher.html")

    def test_sign_up_form_teacher_get_html(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('signup_form_teacher'))
        self.assertContains(response,'<div class="card-headergreen">Teacher sign up</div>')

    def test_sign_up_form_teacher_post_response(self):
        response=self.client.post(reverse('signup_form_teacher'),
        {'username': 'teacher2', 'password1': 'pass1234', 'password2': 'pass1234'}, follow=True)
        self.assertEqual(response.status_code, 200)

    # check that when a new user signs up, a new User is added to the database
    def test_sign_up_form_teacher_post_count_users(self):
        count = User.objects.all().count()
        response=self.client.post(reverse('signup_form_teacher'),
        {'username': 'teacher2', 'password1': 'pass1234', 'password2': 'pass1234'})
        count2 = User.objects.all().count()
        self.assertEqual(count2, count+1)

    # check that when a new teacheruser signs up a new TeacherProfile is added to the database
    def test_sign_up_form_teacher_post_count_teachers(self):
        count = TeacherProfile.objects.all().count()
        response=self.client.post(reverse('signup_form_teacher'),
        {'username': 'teacher2', 'password1': 'pass1234', 'password2': 'pass1234'})
        count2 = TeacherProfile.objects.all().count()
        self.assertEqual(count2, count+1)

    def test_sign_up_form_teacher_post_template(self):
        response=self.client.post(reverse('signup_form_teacher'),
        {'username': 'teacher2', 'password1': 'pass1234', 'password2': 'pass1234'}, follow=True)
        self.assertTemplateUsed(response, 'custom_users/edit_teacher.html')

    def test_sign_up_form_teacher_post_html(self):
        response=self.client.post(reverse('signup_form_teacher'),
        {'username': 'teacher2', 'password1': 'pass1234', 'password2': 'pass1234'}, follow=True)
        self.assertContains(response, '<div class="card-headergreen">Add Teacher Details</div>')

    # test home view when student user logged in
    def test_home_student_response(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_home_student_template(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('home'), follow=True)
        self.assertTemplateUsed(response, 'custom_users/welcome_student.html')

    def test_home_student_html(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('home'), follow=True)
        self.assertContains(response, '<h5><strong>Welcome Student:</strong> student2</h5>')

    # test home view when teacher user logged in
    def test_home_teacher_response(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_teacher_template(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'custom_users/welcome_teacher.html')

    def test_home_teacher_html(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('home'))
        self.assertContains(response, '<h5>Welcome Teacher: teacher</h5>')

    # test home view when user not logged in
    def test_home_anon_response(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_anon_template(self):
        response=self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'signup.html')

    def test_home_anon_html(self):
        response=self.client.get(reverse('home'))
        self.assertContains(response, '<h3>Sign up for a free account</h3>')

    # test edit_student view GET and POST requests
    def test_edit_student_get_response(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('edit_student'))
        self.assertEqual(response.status_code, 200)

    def test_edit_student_post_response(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('edit_student'), {'school': '1', 'teacher': '1', 'class_id':'1' })
        self.assertEqual(response.status_code, 200)

    # check edit_student view changed the user's school details
    def test_edit_student_post_response_update_details(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.post(reverse('edit_student'), {'school': '1', 'teacher': '1', 'class_id':'1' })
        student = StudentProfile.objects.get(user_id = 3)
        self.assertEqual(student.school.name, "Freedom Highschool")

    def test_edit_student_get_template(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('edit_student'))
        self.assertTemplateUsed(response, 'custom_users/edit_student.html')

    def test_edit_student_post_template(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.post(reverse('edit_student'), {'school': '1', 'teacher': '1', 'class_id':'1' }, follow = True)
        self.assertTemplateUsed(response, 'custom_users/student_details_added.html')

    def test_edit_student_get_html(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('edit_student'))
        self.assertContains(response, '<div class="card-headergreen">Add Student Details</div>')

    def test_edit_student_post_html(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.post(reverse('edit_student'), {'school': '1', 'teacher': '1', 'class_id':'1' }, follow = True)
        self.assertContains(response, '<div class="card-headergreen">Student Details Added</div>')

    # check edit_teacher view. GET and POST requests
    def test_edit_teacher_get_response(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('edit_teacher'))
        self.assertEqual(response.status_code, 200)

    def test_edit_teacher_post_response(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.post(reverse('edit_teacher'),
        {'name': '2', 'class_name': 'SomeClass'})
        self.assertEqual(response.status_code, 200)

    # check edit_teacher view changed the user's school details
    def test_edit_teacher_post_response_update_details(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.post(reverse('edit_teacher'), {'name': '2', 'class_name': 'SomeClass'})
        teacher = TeacherProfile.objects.get(user_id = 1)
        self.assertEqual(teacher.school.name, "SomeSchool")

    def test_edit_teacher_get_template(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('edit_teacher'))
        self.assertTemplateUsed(response, 'custom_users/edit_teacher.html')

    def test_edit_teacher_post_template(self):
        self.client.force_login(User.objects.get(id=1))
        teacher = TeacherProfile.objects.get(user_id = 1)
        response=self.client.post(reverse('edit_teacher'),
        {'name': '2', 'class_name': 'SomeClass'})
        self.assertTemplateUsed(response, 'custom_users/teacher_details_added.html')

    def test_edit_teacher_get_html(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('edit_teacher'))
        self.assertContains(response, '<div class="card-headergreen">Add Teacher Details</div>')

    def test_edit_teacher_post_html(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.post(reverse('edit_teacher'),
        {'name': '2', 'class_name': 'SomeClass'})
        self.assertContains(response, '<div class="card-headergreen">Teacher Details Added</div>')

    # test add_school view GET and POST requests
    def test_add_school_get_response(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('add_school'))
        self.assertEqual(response.status_code, 200)

    def test_add_school_post_response(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.post(reverse('add_school'), {'name': 'schoolName', 'post_code': 'my_postcode'})
        self.assertEqual(response.status_code, 200)

    def test_add_school_get_template(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('add_school'))
        self.assertTemplateUsed(response, 'custom_users/add_school.html')

    def test_add_school_post_template(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.post(reverse('add_school'), {'name': 'schoolName', 'post_code': 'my_postcode'})
        self.assertTemplateUsed(response, 'custom_users/teacher_details_added.html')

    def test_add_school_get_html(self):
        self.client.force_login(User.objects.get(id=3))
        response=self.client.get(reverse('add_school'))
        self.assertContains(response, '<div class="card-headergreen">Add School</div>')

    def test_add_school_post_html(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.post(reverse('add_school'), {'name': 'schoolName', 'post_code': 'my_postcode'})
        self.assertContains(response, '<div class="card-headergreen">Teacher Details Added</div>')

    # Test student_details_added view
    def test_student_details_added_response(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('student_details_added'))
        self.assertEqual(response.status_code, 200)

    def test_student_details_added_template(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('student_details_added'))
        self.assertTemplateUsed(response, 'custom_users/student_details_added.html')

    def test_student_details_added_html(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('student_details_added'))
        self.assertContains(response, '<div class="card-headergreen">Student Details Added</div>')

    # Test teacher_details_added view
    def test_teacher_details_added_response(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('teacher_details_added'))
        self.assertEqual(response.status_code, 200)

    def test_teacher_details_added_template(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('teacher_details_added'))
        self.assertTemplateUsed(response, 'custom_users/teacher_details_added.html')

    def test_teacher_details_added_html(self):
        self.client.force_login(User.objects.get(id=1))
        response=self.client.get(reverse('teacher_details_added'))
        self.assertContains(response, '<div class="card-headergreen">Teacher Details Added</div>')

    # Test load_ajax_classes view
    def test_load_ajax_classes_response(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('ajax_load_classes'))
        self.assertEqual(response.status_code, 200)

    def test_load_ajax_classes_template(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('ajax_load_classes'))
        self.assertTemplateUsed(response, 'custom_users/ajax_load_classes.html')

    def test_load_ajax_classes_html(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('ajax_load_classes'))
        self.assertContains(response, '<option value="">---------</option>')

    # Test load_ajax_teachers view
    def test_load_ajax_teachers_response(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('ajax_load_teachers'))
        self.assertEqual(response.status_code, 200)

    def test_load_ajax_teachers_template(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('ajax_load_teachers'))
        self.assertTemplateUsed(response, 'custom_users/ajax_load_teachers.html')

    def test_load_ajax_teachers_html(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('ajax_load_teachers'))
        self.assertContains(response, '<option value="">---------</option>')
