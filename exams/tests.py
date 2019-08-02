from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.utils.decorators import method_decorator
from custom_users.models import Class_id, StudentProfile, TeacherProfile
from .models import Answer, Exam, Formula_Question, Level, MCQ_Question, Question, UserAnswer, Written_Question
from .utils import calculate_percentage, create_user_answer, get_corrections_formula, get_corrections_mcq, get_corrections_written, get_formula
from .views import dotest, show_result, review

class ExamsTest(TestCase):
    # set up testing database
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username ="teacher", password="mypass")
        User.objects.create(username ="student1", password="mypass")
        User.objects.create(username ="student2", password="mypass")
        user1 = User.objects.get(id=1)
        user2 = User.objects.get(id=2)
        user3 = User.objects.get(id=3)
        Class_id.objects.create(id = 1, name = "9y3", teacher_id = 1)
        class_id = Class_id.objects.get(id=1)
        TeacherProfile.objects.create(user = user1, is_teacher = True)
        teacher = TeacherProfile.objects.get(user_id=1)
        StudentProfile.objects.create(user = user2, teacher = teacher, class_id = class_id)
        student1 = StudentProfile.objects.get(user_id=2)
        StudentProfile.objects.create(user = user3, teacher = teacher, class_id = class_id)
        student2 = StudentProfile.objects.get(user_id=3)
        Level.objects.create(title = "1")
        level_1 = Level.objects.get(id = 1)
        Exam.objects.create(level = level_1, title = "Test Exam Title 1")
        exam1 = Exam.objects.get(id=1)
        MCQ_Question.objects.create(exam = exam1, text = "What is my favourite colour? ")
        question1 = MCQ_Question.objects.get(id=1)
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
        Written_Question.objects.create(exam = exam1, text = "What is my favourite film? ")
        question2 = Written_Question.objects.get(id=2)
        Answer.objects.create(question = question2, text = "Shrek", correct = True, correct_spelling = True)
        Answer.objects.create(question = question2, text = "Shrak", correct = True, correct_spelling = False)
        UserAnswer.objects.create(question = question2, user_answer = "   Shrek    ", user = student2)
        UserAnswer.objects.create(question = question2, user_answer = "   Shrak ", user = student1)
        Formula_Question.objects.create(exam = exam1, text = "What is the chemical formula for water? ")
        question3 = Formula_Question.objects.get(id=3)
        Answer.objects.create(question = question3, text = "H2O", correct = True, correct_spelling = True)
        UserAnswer.objects.create(question = question3, user_answer = "h2o", user = student2)
        UserAnswer.objects.create(question = question3, user_answer = "H2O", user = student1)

    def setUp(self):
        # set up TestCase
        self.level_1 = Level.objects.get(id = 1)
        self.exam1 = Exam.objects.get(id=1)
        self.useranswer = UserAnswer.objects.get(id=1)
        self.question1 = Question.objects.get(id=1)
        self.option1 = Answer.objects.get(id=1)
        self.option4 = Answer.objects.get(id=4)
        self.user_answer = UserAnswer.objects.get(id=1)
        self.client = Client()
        self.student2 = StudentProfile.objects.get(user_id=3)
        self.student1 = StudentProfile.objects.get(user_id=2)
        self.user = User.objects.get(id=3)
        self.questions = Question.objects.all()


    # Model Tests
    # test the __str__ methods for all the models in exams

    def test_level_str(self):
        self.assertEquals(self.level_1.__str__(), "1")

    def test_exam_str(self):
        self.assertEquals(self.exam1.__str__(), "Test Exam Title 1")

    def test_question_str(self):
        self.assertEquals(self.question1.__str__(), "What is my favourite colour? ")

    def test_answer_str(self):
        self.assertEquals(self.option1.__str__(), "Yellow")

    def test_useranswer_str(self):
        self.assertEquals(self.user_answer.__str__(), "Green")


    # views tests
    # check the dotest get request returns a valid response
    def test_get_do_test_response_code(self):
        response = self.client.get(reverse('dotest', args=[1,]))
        self.assertEquals(response.status_code, 200)

    # check the dotest get method returns the expected template
    def test_get_do_test_template_used(self):
        response = self.client.get(reverse('dotest', args=[1,]))
        self.assertTemplateUsed(response, 'exams/dotest.html')

    # check the dotest get request returned template contains the expected html
    def test_get_do_test_template_contains(self):
        response = self.client.get(reverse('dotest', args=[1,]))
        self.assertContains(response, "<p><strong>What is my favourite colour? </strong></p>")

    # check the utils.create_user_answer method adds a UserAnswer to the database
    def test_create_user_answer(self):
        request = {'csrfmiddlewaretoken': 'mihQP', '1': '1'}
        count = UserAnswer.objects.all().count()
        create_user_answer(request, self.student2 )
        count_2 = UserAnswer.objects.all().count()
        self.assertEquals(count_2, count+1)

    # check the dotest post request returns a valid response
    def test_post_dotest(self):
        request_param = {'csrfmiddlewaretoken': 'mihQP', '1': '1'}
        rf = RequestFactory()
        url = reverse('dotest', args=[1,])
        request = rf.post(url, request_param )
        request.user = self.user
        response = dotest(request, 1)
        self.assertEquals(response.status_code, 200)

    # check the show_result get request returns a valid response
    def test_get_show_resuts(self):
        request_param = {}
        rf = RequestFactory()
        url = reverse('show_result', args=[1,])
        request = rf.get(url, request_param )
        request.user = self.user
        response = show_result(request, 1)
        self.assertEquals(response.status_code, 200)

    # check the review get request returns a valid response
    def test_get_review(self):
        request_param = {}
        rf = RequestFactory()
        url = reverse('review', args=[1,])
        request = rf.get(url, request_param )
        request.user = self.user
        response = review(request, 1)
        self.assertEquals(response.status_code, 200)

    #test utils.calculate_percentage helper method
    def test_calculate_percentage_1(self):
        questions = Question.objects.all()
        percentage = calculate_percentage(questions, self.student2.user_id, 1)
        self.assertEquals(percentage, 33)

    def test_calculate_percentage_2(self):
        questions = Question.objects.all()
        percentage = calculate_percentage(questions, self.student1.user_id, 1)
        self.assertEquals(percentage, 100)

    #test utils.get_corrections helper method
    def test_get_corrections_mcq(self):
        questions = Question.objects.all()
        corrections = get_corrections_mcq(self.student2.user_id, 1)
        self.assertEquals(corrections, {"What is my favourite colour? ": "Green"})
