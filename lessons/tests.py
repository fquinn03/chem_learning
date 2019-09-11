from django.test import Client, TestCase
from django.urls import reverse
from custom_users.models import User, StudentProfile, TeacherProfile
from exams.models import CompletedExam, Exam
from exams.utils import get_level, get_next_lesson
from .models import Lesson
from .utils import add_lesson_completed

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
        exam1 = Exam.objects.create(title = "test_exam1", level = 2)
        User.objects.create_user(id = 2, username = "student1", password="student1_pass")
        User.objects.create(id = 3, username = "student2", password="student_pass")
        User.objects.create(id = 4, username = "student3", password="student_pass")
        User.objects.create(id = 5, username = "student4", password="student_pass")
        User.objects.create(id = 6, username = "student5", password="student_pass")
        User.objects.create(id = 7, username = "student6", password="student_pass")
        User.objects.create_user(id = 8, username = "student7", password="student_pass")
        User.objects.create_user(id = 9, username = "teacher", password="teacher_pass")
        studentuser = User.objects.get(id = 2)
        studentuser1 = User.objects.get(id = 3)
        studentuser2 = User.objects.get(id = 4)
        studentuser3 = User.objects.get(id = 5)
        studentuser4 = User.objects.get(id = 6)
        studentuser5 = User.objects.get(id = 7)
        studentuser7 = User.objects.get(id = 8)
        StudentProfile.objects.create(user = studentuser, level = 1,
         details_added = True, signup_quiz_completed = True, next_lesson_id=1, next_exam_id=1)
        StudentProfile.objects.create(user = studentuser1, level = 1, next_lesson_id=2 )
        StudentProfile.objects.create(user = studentuser2, level = 2, attempt = 3 )
        StudentProfile.objects.create(user = studentuser3, level = 2, attempt = 3 )
        StudentProfile.objects.create(user = studentuser4, level = 1, attempt = 2 )
        StudentProfile.objects.create(user = studentuser5, level = 1, attempt = 2 )
        StudentProfile.objects.create(user = studentuser7, level = 5, next_lesson_id = 7,
        signup_quiz_completed = True, details_added = True, )
        TeacherProfile.objects.create(user_id = 9, details_added = True)
        student1 = StudentProfile.objects.get(user_id = 2)
        student2 = StudentProfile.objects.get(user_id = 3)
        student3 = StudentProfile.objects.get(user_id = 4)
        student4 = StudentProfile.objects.get(user_id = 5)
        student5 = StudentProfile.objects.get(user_id = 6)
        student6 = StudentProfile.objects.get(user_id = 7)
        Lesson.objects.create(level = 1, title = "test_lesson_1_1", link = "www.testlink1.com")
        Lesson.objects.create(level = 1, title = "test_lesson_1_2", link = "www.testlink2.com")
        Lesson.objects.create(level = 1, title = "test_lesson_1_3", link = "www.testlink3.com")
        Lesson.objects.create(level = 2, title = "test_lesson_2_1", link = "www.testlink1.com")
        Lesson.objects.create(level = 2, title = "test_lesson_2_2", link = "www.testlink2.com")
        Lesson.objects.create(level = 2, title = "test_lesson_2_3", link = "www.testlink3.com")
        lesson1 = Lesson.objects.get(id = 1)
        lesson2 = Lesson.objects.get(id = 2)
        lesson3 = Lesson.objects.get(id = 3)
        lesson4 = Lesson.objects.get(id = 4)
        lesson5 = Lesson.objects.get(id = 5)
        lesson6 = Lesson.objects.get(id = 6)
        student2.completed_lessons.add(lesson1)
        student3.completed_lessons.add(lesson1)
        student3.completed_lessons.add(lesson2)
        student3.completed_lessons.add(lesson3)
        student4.completed_lessons.add(lesson1)
        student5.completed_lessons.add(lesson4)
        student6.completed_lessons.add(lesson1)
        student6.completed_lessons.add(lesson2)
        student6.completed_lessons.add(lesson3)
        CompletedExam.objects.create(user = student3, exam = exam1, level = 2, percentage = 35)
        CompletedExam.objects.create(user = student4, exam = exam1, level = 2, percentage = 45)
        CompletedExam.objects.create(user = student5, exam = exam1, level = 1, percentage = 90)
        CompletedExam.objects.create(user = student6, exam = exam1, level = 1, percentage = 63)
    def setUp(self):
    # set up Lessons TestCase
        self.lesson = Lesson.objects.get(id=1)
        self.client = Client()
        self.client.login(username = 'student1', password = 'student1_pass')
        self.student1 = StudentProfile.objects.get(user_id = 2)
        self.student7 = StudentProfile.objects.get(user_id = 8)

    """
    Tests for get_next_lesson()
    if user goes back level and they have previously completed all Lessons
    check all past completed lessons are deleted so they can start again
    """
    def test_go_back_level_delete_completed_levels(self):
        get_level(4)
        get_next_lesson(4)
        self.assertEqual(StudentProfile.objects.get(user_id = 4).level, 1)
        self.assertEqual(StudentProfile.objects.get(user_id = 4).next_lesson_id, 1)

    """
    if user goes back level and they have not previously completed all Lessons
    they continue where they left off
    """
    def test_go_back_level_and_continue_lessons1(self):
        get_level(5)
        get_next_lesson(5)
        self.assertEqual(StudentProfile.objects.get(user_id = 5).level, 1)
        self.assertEqual(StudentProfile.objects.get(user_id = 5).next_lesson_id, 2)

    """
    if user goes up a level and they have previously completed a Lesson
    in that level they continue where they left off
    """
    def test_go_back_level_and_continue_lessons2(self):
        get_level(6)
        get_next_lesson(6)
        self.assertEqual(StudentProfile.objects.get(user_id = 6).level, 2)
        self.assertEqual(StudentProfile.objects.get(user_id = 6).next_lesson_id, 5)

    """
    if user stays on the same level and they have previously completed all Lessons
    in that level they restart the lessons.
    """
    def test_go_back_level_and_continue_lessons_again(self):
        get_level(7)
        get_next_lesson(7)
        self.assertEqual(StudentProfile.objects.get(user_id = 7).level, 1)
        self.assertEqual(StudentProfile.objects.get(user_id = 7).next_lesson_id, 1)

    # test add_lesson_completed.utils
    def test_add_lesson_completed(self):
        add_lesson_completed(self.student1.user_id)
        completed_lessons = self.student1.completed_lessons
        self.assertQuerysetEqual(self.student1.completed_lessons.all(),  ["<Lesson: test_lesson_1_1>"])

    def test_add_lesson_completed_2(self):
        add_lesson_completed(self.student1.user_id)
        completed_lessons = self.student1.completed_lessons
        add_lesson_completed(self.student1.user_id)
        completed_lessons = self.student1.completed_lessons
        self.assertQuerysetEqual(self.student1.completed_lessons.all().order_by('id'),  ['<Lesson: test_lesson_1_1>', '<Lesson: test_lesson_1_2>'])

    """
    Models Tests
    """
    # test str method
    def test_str(self):
        self.assertEqual(self.lesson.__str__(), "test_lesson_1_1")

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
    def test_complete_lesson_as_student(self):
        self.client.login(username = "student1", password="student1_pass")
        response = self.client.get(reverse('complete_lesson'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/view_lesson.html')
        self.assertContains(response, "<h5>Lesson Title: test_lesson_1_1</h5>")

    def test_complete_lesson_as_teacher(self):
        self.client.login(username = "teacher", password="teacher_pass")
        response = self.client.get(reverse('complete_lesson'), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "custom_users/welcome_teacher.html")
        self.assertContains(response, "<h5>Welcome Teacher: teacher</h5>")

    def test_complete_lesson_as_anon(self):
        self.client.logout()
        response = self.client.get(reverse('complete_lesson'), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")
        self.assertContains(response, '<h3 class="green_header">Welcome to ChemLearning</h3>')

    # test mark_lesson_as_complete view
    def test_mark_lesson_as_complete_as_student(self):
        self.client.login(username = "student1", password="student1_pass")
        response = self.client.get(reverse('mark_lesson_as_complete'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('mark_lesson_as_complete'), follow=True)
        self.assertTemplateUsed(response, 'lessons/view_lesson.html')
        self.assertContains(response, "<h5>Lesson Title: test_lesson_1_3</h5>")

    def test_mark_lesson_as_complete_as_teacher(self):
        self.client.login(username = "teacher", password="teacher_pass")
        response = self.client.get(reverse('complete_lesson'), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "custom_users/welcome_teacher.html")
        self.assertContains(response, "<h5>Welcome Teacher: teacher</h5>")

    def test_mark_lesson_as_complete_as_anon(self):
        self.client.logout()
        response = self.client.get(reverse('complete_lesson'), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")
        self.assertContains(response, '<h3 class="green_header">Welcome to ChemLearning</h3>')

    # test take_the_next_quiz view
    def test_take_the_next_quiz_as_student(self):
        response = self.client.get(reverse('take_the_next_quiz'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('take_the_next_quiz'), follow=True)
        self.assertTemplateUsed(response, 'exams/dotest.html')
        self.assertContains(response, "<h5>test_exam1</h5>")

    def test_take_the_next_quiz_as_teacher(self):
        self.client.login(username = "teacher", password="teacher_pass")
        response = self.client.get(reverse('take_the_next_quiz'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "custom_users/welcome_teacher.html")
        self.assertContains(response, "<h5>Welcome Teacher: teacher</h5>")

    def test_take_the_next_quiz_as_anon(self):
        self.client.logout()
        response = self.client.get(reverse('take_the_next_quiz'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")
        self.assertContains(response, '<h3 class="green_header">Welcome to ChemLearning</h3>')

    # test go_back_to_welcome_student view
    def test_go_back_to_welcome_student_as_student(self):
        response = self.client.get(reverse('go_back_to_welcome_student'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('go_back_to_welcome_student'), follow=True)
        self.assertTemplateUsed(response, 'custom_users/welcome_student.html')
        self.assertContains(response, "<h5><strong>Welcome Student:</strong> student1</h5>")

    def test_go_back_to_welcome_student_as_teacher(self):
        self.client.login(username = "teacher", password="teacher_pass")
        response = self.client.get(reverse('go_back_to_welcome_student'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "custom_users/welcome_teacher.html")
        self.assertContains(response, "<h5>Welcome Teacher: teacher</h5>")

    def test_go_back_to_welcome_student_as_anon(self):
        self.client.logout()
        response = self.client.get(reverse('take_the_next_quiz'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")
        self.assertContains(response, '<h3 class="green_header">Welcome to ChemLearning</h3>')

    """
    Test if student.next_lesson does not exist.
    Student is finished the course, student.level > levels in the course(15)
    """
    def test_lesson_does_not_exist(self):
        self.assertEqual(add_lesson_completed(8), None)

    def test_complete_lesson_student_finished_response(self):
        self.client.login(username="student7", password = "student_pass")
        response = self.client.get(reverse('complete_lesson'))
        self.assertEqual(response.status_code, 302)

    def test_complete_lesson_student_finished_template(self):
        self.client.login(username="student7", password = "student_pass")
        response = self.client.get(reverse('complete_lesson'), follow = True )
        self.assertTemplateUsed(response, 'exams/congratulations.html')

    def test_complete_lesson_student_finished_html(self):
        self.student7.next_lesson_id = 3
        self.client.login(username="student7", password = "student_pass")
        response = self.client.get(reverse('complete_lesson'), follow = True )
        self.assertContains(response, "<h1 class='gold .animation-lightSpeedin'>")
