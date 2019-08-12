from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.utils.decorators import method_decorator
from custom_users.models import Class_id, StudentProfile, TeacherProfile
from lessons.models import Lesson
from .models import (Answer, Exam, Formula_Question, MCQ_Question, Question,
UserAnswer, Written_Question, CompletedExam)
from .utils import (calculate_percentage, create_exam_completed_entry,
create_user_answer, get_corrections_formula, get_corrections_mcq,
get_corrections_written, get_corrections_written, get_formula,
get_level)
from .views import dotest, show_result, review

"""
Unit tests for all of the exams views and utils.
NOTE: force_login method is used instead of login() when a test requires a user be logged in
and the details of how a user logged in aren’t important.
This method is faster than login() since the expensive password hashing algorithms are bypassed
"""

class ExamsTest(TestCase):
    # set up testing database
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username ="teacher", password="mypass")
        User.objects.create(username ="student1", password="mypass")
        User.objects.create(username ="student2", password="mypass")
        User.objects.create(username ="student3", password="mypass")
        User.objects.create(username ="student4", password="mypass")
        User.objects.create(username ="student5", password="mypass")
        User.objects.create(username ="student6", password="mypass")
        User.objects.create(username ="student7", password="mypass")
        user1 = User.objects.get(id=1)
        user2 = User.objects.get(id=2)
        user3 = User.objects.get(id=3)
        user4 = User.objects.get(id=4)
        user5 = User.objects.get(id=5)
        user6 = User.objects.get(id=6)
        user7 = User.objects.get(id=7)
        user8 = User.objects.get(id=8)
        Class_id.objects.create(id = 1, name = "9y3", teacher_id = 1)
        class_id = Class_id.objects.get(id=1)
        TeacherProfile.objects.create(user = user1, is_teacher = True)
        teacher = TeacherProfile.objects.get(user_id=1)
        StudentProfile.objects.create(user = user2, teacher = teacher, class_id = class_id, level = 1, attempt = 1)
        student1 = StudentProfile.objects.get(user_id=2)
        StudentProfile.objects.create(user = user3, teacher = teacher, class_id = class_id, level = 2, attempt = 1)
        student2 = StudentProfile.objects.get(user_id=3)
        StudentProfile.objects.create(user = user4, teacher = teacher, class_id = class_id, level = 1, attempt = 3)
        student3 = StudentProfile.objects.get(user_id=4)
        StudentProfile.objects.create(user = user5, teacher = teacher, class_id = class_id, level = 4, attempt = 3)
        student4 = StudentProfile.objects.get(user_id=5)
        StudentProfile.objects.create(user = user6, teacher = teacher, class_id = class_id, level = 4, attempt = 3)
        student5 = StudentProfile.objects.get(user_id=6)
        StudentProfile.objects.create(user = user7, teacher = teacher, class_id = class_id, level = 5, attempt = 2)
        student6 = StudentProfile.objects.get(user_id=7)
        StudentProfile.objects.create(user = user8, teacher = teacher, class_id = class_id, level = 7, attempt = 2)
        student7 = StudentProfile.objects.get(user_id=8)
        Exam.objects.create(level = 1, title = "Test Exam Title 1")
        Exam.objects.create(level = 0, title = "signup_quiz")
        Exam.objects.create(level = 2, title = "Test Exam Title 2")
        Exam.objects.create(level = 3, title = "Test Exam Title 3")
        exam1 = Exam.objects.get(id=1)
        exam2 = Exam.objects.get(id=2)
        exam3 = Exam.objects.get(id=3)
        exam4 = Exam.objects.get(id=4)
        MCQ_Question.objects.create(text = "What is my favourite colour? ")
        question1 = MCQ_Question.objects.get(id=1)
        question1.exam.add(exam1)
        Answer.objects.create(question = question1, text = "Yellow", correct = False)
        Answer.objects.create(question = question1, text = "Blue", correct = False)
        Answer.objects.create(question = question1, text = "Red", correct = False)
        Answer.objects.create(question = question1, text = "Green", correct = True)
        option1 = Answer.objects.get(id=1)
        option2 = Answer.objects.get(id=2)
        option3 = Answer.objects.get(id=3)
        option4 = Answer.objects.get(id=4)
        UserAnswer.objects.create(question = question1, user_answer = option4, user = student1)
        UserAnswer.objects.create(question = question1, user_answer = option2, user = student2)
        useranswer = UserAnswer.objects.get(id=1)
        Written_Question.objects.create(text = "What is my favourite film? ")
        question2 = Written_Question.objects.get(id=2)
        question2.exam.add(exam1)
        Answer.objects.create(question = question2, text = "Shrek", correct = True, correct_spelling = True)
        Answer.objects.create(question = question2, text = "Shrak", correct = True, correct_spelling = False)
        UserAnswer.objects.create(question = question2, user_answer = "   Shrek    ", user = student2)
        UserAnswer.objects.create(question = question2, user_answer = "   Shrak ", user = student1)
        Formula_Question.objects.create(text = "What is the chemical formula for water? ")
        question3 = Formula_Question.objects.get(id=3)
        question3.exam.add(exam1)
        Answer.objects.create(question = question3, text = "H2O", correct = True, correct_spelling = True)
        UserAnswer.objects.create(question = question3, user_answer = "h2o", user = student2)
        UserAnswer.objects.create(question = question3, user_answer = "H2O", user = student1)
        CompletedExam.objects.create(user = student1, exam = exam1, level = 1, percentage =100)
        CompletedExam.objects.create(user = student1, exam = exam2, level = 0, percentage = 33)
        CompletedExam.objects.create(user = student3, exam = exam1, level = 1, percentage = 55)
        CompletedExam.objects.create(user = student3, exam = exam3, level = 2, percentage = 85)
        CompletedExam.objects.create(user = student4, exam = exam4, level = 4, percentage = 0)
        CompletedExam.objects.create(user = student2, exam = exam3, level = 2, percentage = 45)
        CompletedExam.objects.create(user = student6, exam = exam3, level = 5, percentage = 45)
        CompletedExam.objects.create(user = student6, exam = exam4, level = 5, percentage = 65)
        CompletedExam.objects.create(user = student7, exam = exam1, level = 7, percentage = 0)
        CompletedExam.objects.create(user = student7, exam = exam2, level = 7, percentage = 80)
        CompletedExam.objects.create(user = student7, exam = exam3, level = 7, percentage = 85)
        Lesson.objects.create(level = 1, title = "a lesson")

    def setUp(self):
        # set up Exams TestCase
        self.exam1 = Exam.objects.get(id=1)
        self.exam4 = Exam.objects.get(id=4)
        self.useranswer = UserAnswer.objects.get(id=1)
        self.question1 = Question.objects.get(id=1)
        self.option1 = Answer.objects.get(id=1)
        self.option4 = Answer.objects.get(id=4)
        self.user_answer = UserAnswer.objects.get(id=1)
        self.client = Client()
        self.student2 = StudentProfile.objects.get(user_id=3)
        self.student1 = StudentProfile.objects.get(user_id=2)
        self.student3 = StudentProfile.objects.get(user_id=4)
        self.student4 = StudentProfile.objects.get(user_id=5)
        self.student1.level = 1
        self.student2.level = 1
        self.user = User.objects.get(id=3)
        self.questions = Question.objects.all()

    """
    Models Tests
    """
    # test the __str__ methods for all the models in exams
    def test_exam_str(self):
        self.assertEqual(self.exam1.__str__(), "1 Test Exam Title 1")

    def test_question_str(self):
        self.assertEqual(self.question1.__str__(), "What is my favourite colour? ")

    def test_answer_str(self):
        self.assertEqual(self.option1.__str__(), "Yellow")

    def test_useranswer_str(self):
        self.assertEqual(self.user_answer.__str__(), "Green")

    def test_completed_exam_str(self):
        self.assertEqual(CompletedExam.objects.get(id = 1).__str__(), "student1 Test Exam Title 1" )

    """
    Views and Template testing

    Each view is tested for expected response using using GET requests
    (and POST requests where relevant).

    Template rendered is tested using assertTemplateUsed()
    This checks the correct template is rendered for logged in
    user type and the type of request.

    The template and context are tested using assertContains(), to
    ensure the correct template has been rendered with the correct
    context data for logged in user where relevant.

    Additional testing for individual views is added and explained
    where necessary.
    """
    # test dotest view. GET and POST requests
    def test_do_test_get_response_code(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.get(reverse('dotest', args=[1,]))
        self.assertEqual(response.status_code, 200)

    def test_do_test_get_template_used(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.get(reverse('dotest', args=[1,]))
        self.assertTemplateUsed(response, 'exams/dotest.html')

    def test_do_test_get_html(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.get(reverse('dotest', args=[1,]))
        self.assertContains(response, "<p><strong>What is my favourite colour? </strong></p>")

    def test_do_test_post_response_code(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.post(reverse('dotest', args=[1,]),
        {'csrfmiddlewaretoken': 'flsff','1': 'Green', '2': 'jaws'})
        self.assertEqual(response.status_code, 200)

    def test_do_test_post_template_used(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.post(reverse('dotest', args=[1,]),
        {'csrfmiddlewaretoken': 'flsff','1': 'Green', '2': 'jaws'})
        self.assertTemplateUsed(response, 'exams/finish_test.html')

    def test_do_test_post_html(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.post(reverse('dotest', args=[1,]),
        {'csrfmiddlewaretoken': 'flsff','1': 'Green', '2': 'jaws'})
        self.assertContains(response, "<h5>You have submitted your answers to Test Exam Title 1<br><br/></h5>")

    # test show_result view.
    def test_show_result_get_response_code(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.get(reverse('show_result', args=[1,]))
        self.assertEqual(response.status_code, 200)

    def test_show_result_get_template_used(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.get(reverse('show_result', args=[1,]))
        self.assertTemplateUsed(response, 'exams/show_result.html')

    def test_show_result_get_html(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.get(reverse('show_result', args=[1,]))
        self.assertContains(response, "<h5>You scored: 33% on Test Exam Title 1<br><br/></h5>")

    # test review view
    def test_review_get_response_code(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.get(reverse('review', args=[1,]))
        self.assertEqual(response.status_code, 200)

    def test_review_get_template_used(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.get(reverse('review', args=[1,]))
        self.assertTemplateUsed(response, 'exams/review.html')

    def test_review_get_html(self):
        self.client.force_login(User.objects.get(id=3))
        response = self.client.get(reverse('review', args=[1,]))
        self.assertContains(response, "<h5>Questions you need to review</h5>")

    # test test_do_quiz_signup view. GET and POST requests
    def test_do_quiz_signup_get_response(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('do_signup_quiz'))
        self.assertEqual(response.status_code, 200)

    def test_do_quiz_signup_get_template(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('do_signup_quiz'))
        self.assertTemplateUsed(response, 'custom_users/do_signup_quiz.html')

    def test_do_quiz_signup_get_html(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.get(reverse('do_signup_quiz'))
        self.assertContains(response, '<h5>SignUp Quiz</h5>')

    def test_do_quiz_signup_post_response(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.post(reverse('do_signup_quiz'), {'2':'True', '3': 'True', '4': 'False'}, follow = True)
        self.assertEqual(response.status_code, 200)

    def test_do_quiz_signup_post_student_level_2(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.post(reverse('do_signup_quiz'), {'2':'True', '3': 'True', '4': 'False'}, follow = True)
        student = StudentProfile.objects.get(user_id = 2)
        self.assertEqual(student.level, 2)

    def test_do_quiz_signup_post_student_level_3(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.post(reverse('do_signup_quiz'), {'2':'True', '3': 'True', '4': 'True'}, follow = True)
        student = StudentProfile.objects.get(user_id = 2)
        self.assertEqual(student.level, 3)

    def test_do_quiz_signup_post_template(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.post(reverse('do_signup_quiz'), {'2':'True', '3': 'True', '4': 'False'}, follow = True)
        self.assertTemplateUsed(response, 'custom_users/welcome_student.html')

    def test_do_quiz_signup_post_html(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.post(reverse('do_signup_quiz'), {'2':'True', '3': 'True', '4': 'False'}, follow = True)
        self.assertContains(response, "<h5><strong>Welcome Student:</strong> student1</h5>")

    """
    Utils testing
    """
    # check the utils.create_user_answer method adds a UserAnswer to the database
    def test_create_user_answer(self):
        request = {'csrfmiddlewaretoken': 'mihQP', '1': '1'}
        count = UserAnswer.objects.all().count()
        create_user_answer(request, self.student2 )
        count_2 = UserAnswer.objects.all().count()
        self.assertEqual(count_2, count+1)

    #test utils.calculate_percentage helper method
    def test_calculate_percentage_1(self):
        questions = Question.objects.all()
        percentage = calculate_percentage(questions, self.student2.user_id, 1)
        self.assertEqual(percentage, 33)

    def test_calculate_percentage_2(self):
        questions = Question.objects.all()
        percentage = calculate_percentage(questions, self.student1.user_id, 1)
        self.assertEqual(percentage, 100)

    #test utils.get_corrections_mcq helper method
    def test_get_corrections_mcq(self):
        questions = Question.objects.all()
        corrections = get_corrections_mcq(self.student2.user_id, 1)
        self.assertEqual(corrections, {"What is my favourite colour? ": "Green"})

    #test utils.get_corrections_written helper method
    def test_get_corrections_written_incorrect(self):
        questions = Written_Question.objects.all()
        corrections = get_corrections_written(self.student1.user_id, 1)
        self.assertEqual(corrections[0], {})

    def test_get_corrections_written_mispelled(self):
        questions = Written_Question.objects.all()
        corrections = get_corrections_written(self.student1.user_id, 1)
        self.assertEqual(corrections[1], {'What is my favourite film? ': 'Shrek'})

    # test utils.create_exam_completed_entry
    def test_create_exam_completed_entry_student1(self):
        user = StudentProfile.objects.get(user_id=4)
        create_exam_completed_entry(user, self.exam4, 78)
        exam_completed_entry = CompletedExam.objects.get(id = 12)
        self.assertEqual(exam_completed_entry.exam, self.exam4)
        self.assertEqual(exam_completed_entry.percentage, 78)
        self.assertEqual(exam_completed_entry.user.user.username, "student3")
        self.assertEqual(exam_completed_entry.user.user.password, "mypass")

    # test utils.get_level
    # increment level
    def test_get_level_student1(self):
        student1 = StudentProfile.objects.get(user_id = 2)
        get_level(2)
        student1 = StudentProfile.objects.get(user_id = 2)
        self.assertEqual(student1.level, 2)

    # decrement level
    def test_get_level_student4(self):
        student4 = StudentProfile.objects.get(user_id = 5)
        get_level(5)
        student4 = StudentProfile.objects.get(user_id = 5)
        self.assertEqual(student4.level, 3)

    # level stays the same
    def test_get_level_student2(self):
        student2 = StudentProfile.objects.get(user_id = 3)
        get_level(3)
        student2 = StudentProfile.objects.get(user_id = 3)
        self.assertEqual(student2.level, 2)
        self.assertEqual(student2.attempt, 2)

    # don't decrement below level one
    def test_get_level_student3(self):
        student3 = StudentProfile.objects.get(user_id = 4)
        get_level(4)
        student3 = StudentProfile.objects.get(user_id = 4)
        self.assertEqual(student3.level, 1)

    # no exams at that level score = 0, attempst = 0
    def test_get_level_no_exams(self):
        student5 = StudentProfile.objects.get(user_id = 6)
        get_level(6)
        student5 = StudentProfile.objects.get(user_id = 6)
        self.assertEqual(student5.level, 4)
        self.assertEqual(student5.attempt, 0)

    # 2 or more exams weighted mean
    def test_get_level_two_exams(self):
        student6 = StudentProfile.objects.get(user_id = 7)
        get_level(7)
        student6 = StudentProfile.objects.get(user_id = 7)
        self.assertEqual(student6.level, 5)
        self.assertEqual(student6.attempt, 3)

    # 3 or more exams weighted mean
    def test_get_level_three_exams(self):
        student7 = StudentProfile.objects.get(user_id = 8)
        get_level(8)
        student7 = StudentProfile.objects.get(user_id = 8)
        self.assertEqual(student7.level, 8)
        self.assertEqual(student7.attempt, 0)
