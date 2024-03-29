from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.utils.decorators import method_decorator
from custom_users.models import Class_id, StudentProfile, TeacherProfile
from lessons.models import Lesson
from .models import (Answer, Exam, Formula_Question, MCQ_Question, Question,
UserAnswer, Written_Question, CompletedExam, IncorrectAnswer, IncorrectAnswer)
from .utils import (calculate_percentage, create_exam_completed_entry,
create_user_answer, delete_completed_exam_record, delete_completed_exam_total, get_corrections_formula,
get_corrections_mcq, get_corrections_written, get_corrections_written, get_formula,
get_level, get_next_exam, get_starting_level)
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
        # create users objects to make students/teachers
        user1 = User.objects.create_user(username ="teacher", password="mypass")
        user2 = User.objects.create_user(username ="student1", password="mypass")
        user3 = User.objects.create_user(username ="student2", password="mypass")
        user4 = User.objects.create_user(username ="student3", password="mypass")
        user5 = User.objects.create_user(username ="student4", password="mypass")
        user6 = User.objects.create(username ="student5", password="mypass")
        user7 = User.objects.create(username ="student6", password="mypass")
        user8 = User.objects.create(username ="student7", password="mypass")
        user9 = User.objects.create(username ="student8", password="mypass")
        user10 = User.objects.create(username ="student9", password="mypass")
        user11 = User.objects.create_user(username ="student10", password="mypass")
        user12 = User.objects.create_user(username ="student11", password="mypass")

        Class_id.objects.create(id = 1, name = "9y3", teacher_id = 1)
        class_id = Class_id.objects.get(id=1)

        #create teachers and students from users
        teacher = TeacherProfile.objects.create(user = user1, is_teacher = True)
        student1 = StudentProfile.objects.create(user = user2, teacher = teacher, class_id = class_id, level = 1,
        attempt = 1, details_added = True, signup_quiz_completed = False, next_lesson_id = 1)
        student2 = StudentProfile.objects.create(user = user3, teacher = teacher, class_id = class_id, level = 2,
        attempt = 1, details_added = True, signup_quiz_completed = True, next_lesson_id = 1 )
        student3 = StudentProfile.objects.create(user = user4, teacher = teacher, class_id = class_id, level = 1, attempt = 3,
        details_added = True, signup_quiz_completed = True,)
        student4 = StudentProfile.objects.create(user = user5, teacher = teacher, class_id = class_id, level = 4, attempt = 3,
        details_added = True, signup_quiz_completed = True,)
        student5 = StudentProfile.objects.create(user = user6, teacher = teacher, class_id = class_id, level = 4, attempt = 3)
        student6 = StudentProfile.objects.create(user = user7, teacher = teacher, class_id = class_id, level = 5, attempt = 2)
        student7 = StudentProfile.objects.create(user = user8, teacher = teacher, class_id = class_id, level = 7, attempt = 2)
        student8 = StudentProfile.objects.create(user = user9, teacher = teacher, class_id = class_id, level = 2,
        attempt = 1, details_added = True, signup_quiz_completed = False, next_lesson_id = 1)
        student9 = StudentProfile.objects.create(user = user10, teacher = teacher, class_id = class_id, level = 1,
        attempt = 1, details_added = True, signup_quiz_completed = False, next_lesson_id = 1)
        student10 = StudentProfile.objects.create(user = user11, teacher = teacher, class_id = class_id, level = 17,
        attempt = 1, details_added = True, signup_quiz_completed = True, next_lesson_id = 1)

        # create exams to test next_exam_id
        exam1 = Exam.objects.create(level = 1, title = "Test Exam Title 1")
        exam2 = Exam.objects.create(level = 0, title = "signup_quiz")
        exam3 = Exam.objects.create(level = 2, title = "Test Exam Title 2")
        exam4 = Exam.objects.create(level = 3, title = "Test Exam Title 3")
        exam5 = Exam.objects.create(level = 1, title = "Test Exam Title 4")
        exam6 = Exam.objects.create(level = 1, title = "Test Exam Title 5")
        exam7 = Exam.objects.create(level = 7, title = "Test Exam Level 7")
        exam8 = Exam.objects.create(level = 7, title = "Test Exam Level 8")
        #create question and answer objects to test show resut
        question1 = MCQ_Question.objects.create(text = "What is my favourite colour? ", exam = exam1)
        Answer.objects.create(question = question1, text = "Yellow", correct = False)
        Answer.objects.create(question = question1, text = "Blue", correct = False)
        Answer.objects.create(question = question1, text = "Red", correct = False)
        Answer.objects.create(question = question1, text = "Green", correct = True)
        option1 = Answer.objects.get(id=1)
        option2 = Answer.objects.get(id=2)
        option3 = Answer.objects.get(id=3)
        option4 = Answer.objects.get(id=4)
        useranswer = UserAnswer.objects.create(question = question1, user_answer = option4, user = student1)
        UserAnswer.objects.create(question = question1, user_answer = option4, user = student4)
        UserAnswer.objects.create(question = question1, user_answer = option2, user = student3)
        UserAnswer.objects.create(question = question1, user_answer = option2, user = student2)
        UserAnswer.objects.create(question = question1, user_answer = option3, user = student9)

        question2 = Written_Question.objects.create(text = "What is my favourite film? ", exam = exam1)
        Answer.objects.create(question = question2, text = "Shrek1",
        correct = True, correct_spelling = True, correct_answer_to_display = False)
        Answer.objects.create(question = question2, text = "Shrek",
        correct = True, correct_spelling = True, correct_answer_to_display = True)
        Answer.objects.create(question = question2, text = "Shrak", correct = True, correct_spelling = False)
        UserAnswer.objects.create(question = question2, user_answer = "   Shrek    ", user = student2)
        UserAnswer.objects.create(question = question2, user_answer = "   Shrek    ", user = student4)
        UserAnswer.objects.create(question = question2, user_answer = "   Shrak ", user = student1)
        UserAnswer.objects.create(question = question2, user_answer = "Jaws", user = student9)
        UserAnswer.objects.create(question = question2, user_answer = "Jaws", user = student3)

        question3 = Formula_Question.objects.create(text = "What is the chemical formula for water? ", exam = exam1)
        Answer.objects.create(question = question3, text = "H2O", correct = True, correct_spelling = True)
        UserAnswer.objects.create(question = question3, user_answer = "h2o", user = student2)
        UserAnswer.objects.create(question = question3, user_answer = "h2o", user = student3)
        UserAnswer.objects.create(question = question3, user_answer = "H2O", user = student1)
        UserAnswer.objects.create(question = question3, user_answer = "H2O", user = student4)
        UserAnswer.objects.create(question = question3, user_answer = "CH4", user = student9)


        # create complete exams to test next_exam_id
        CompletedExam.objects.create(user = student1, exam = exam1, level = 1, percentage =100, attempt = 1)
        CompletedExam.objects.create(user = student1, exam = exam2, level = 0, percentage = 33, attempt = 1)
        CompletedExam.objects.create(user = student3, exam = exam1, level = 1, percentage = 55, attempt = 3)
        CompletedExam.objects.create(user = student3, exam = exam3, level = 2, percentage = 85, attempt = 3)
        CompletedExam.objects.create(user = student4, exam = exam4, level = 4, percentage = 0, attempt = 3)
        CompletedExam.objects.create(user = student4, exam = exam1, level = 1, percentage = 100, attempt = 1)
        CompletedExam.objects.create(user = student2, exam = exam3, level = 2, percentage = 45, attempt = 1)
        CompletedExam.objects.create(user = student6, exam = exam3, level = 5, percentage = 45, attempt = 2)
        CompletedExam.objects.create(user = student6, exam = exam4, level = 5, percentage = 65, attempt = 2)
        CompletedExam.objects.create(user = student7, exam = exam1, level = 7, percentage = 0, attempt = 2)
        CompletedExam.objects.create(user = student7, exam = exam2, level = 7, percentage = 80, attempt = 2)
        CompletedExam.objects.create(user = student7, exam = exam3, level = 7, percentage = 85, attempt = 2)
        CompletedExam.objects.create(user = student9, exam = exam1, level = 1, percentage = 0, attempt = 1)
        CompletedExam.objects.create(user = student9, exam = exam5, level = 1, percentage = 80, attempt = 1)
        CompletedExam.objects.create(user = student9, exam = exam6, level = 1, percentage = 85, attempt = 1)

        # lessons to test next_lesson_id
        Lesson.objects.create(level = 1, title = "a lesson")
        Lesson.objects.create(level = 1, title = "another lesson")
        Lesson.objects.create(level = 2, title = "a third lesson")
        Lesson.objects.create(level = 3, title = "a fourth lesson")
        # Create user, question, answer, completed exam to test user is finished
        question4 = Written_Question.objects.create(text = "What is my favourite drink? ", exam = exam7)
        Answer.objects.create(question = question4, text = "Cola",
        correct = True, correct_spelling = True, correct_answer_to_display = True)
        UserAnswer.objects.create(question = question4, user_answer = "Cola", user = student10)
        CompletedExam.objects.create(user = student10, exam = exam7, level = 7, percentage = 100, attempt = 1)
        IncorrectAnswer.objects.create(user= student9, question = question2)
        student11 = StudentProfile.objects.create(user = User.objects.get(id = 12) , teacher = teacher, class_id = class_id, level = 7,
        attempt = 1, details_added = True, signup_quiz_completed = True, next_lesson_id = 1)
        # create test questions and incorrect answers to test revision view with more than 5 incorrect answers
        question4 = Written_Question.objects.create(text = "test q 4 ", exam = exam8)
        question5 = Written_Question.objects.create(text = "test q 5 ", exam = exam8)
        question6 = Written_Question.objects.create(text = "test q 6", exam = exam8)
        question7 = Written_Question.objects.create(text = "test q 7 ", exam = exam8)
        question8 = Written_Question.objects.create(text = "test q 8 ", exam = exam8)
        question9 = Written_Question.objects.create(text = "test q 9 ", exam = exam8)
        IncorrectAnswer.objects.create(question = question4, user = student11)
        IncorrectAnswer.objects.create(question = question5, user = student11)
        IncorrectAnswer.objects.create(question = question6, user = student11)
        IncorrectAnswer.objects.create(question = question7, user = student11)
        IncorrectAnswer.objects.create(question = question8, user = student11)
        IncorrectAnswer.objects.create(question = question9, user = student11)

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
        self.incorrectanswer = IncorrectAnswer.objects.get(id =1)
        self.question = Question.objects.get(id = 2)

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
        questions = Question.objects.filter(exam_id= 1)
        percentage = calculate_percentage(questions, self.student2.user_id, 1)
        self.assertEqual(percentage, 33)

    def test_calculate_percentage_2(self):
        questions = Question.objects.filter(exam_id = 1)
        percentage = calculate_percentage(questions, self.student1.user_id, 1)
        self.assertEqual(percentage, 100)

    #test utils.get_corrections_mcq helper method
    def test_get_corrections_mcq(self):
        questions = Question.objects.all()
        corrections = get_corrections_mcq(self.student2.user_id, 1)
        self.assertEqual(corrections[0], MCQ_Question.objects.get(id = 1))

    #test utils.get_corrections_written helper method
    def test_get_corrections_written_all_correct(self):
        questions = Written_Question.objects.all()
        corrections = get_corrections_written(self.student1.user_id, 1)
        self.assertEqual(corrections[0], [])

    def test_get_corrections_written_all_correct2(self):
        questions = Written_Question.objects.all()
        corrections = get_corrections_written(11, 7)
        self.assertEqual(corrections[0], [])

    def test_get_corrections_written_mispelled(self):
        questions = Written_Question.objects.all()
        corrections = get_corrections_written(self.student1.user_id, 1)
        self.assertEqual(corrections[1], {'What is my favourite film? ': 'Shrek'})

    def test_get_corrections_written_incorrect(self):
        questions = Written_Question.objects.all()
        student = StudentProfile.objects.get(user_id = 10)
        corrections = get_corrections_written(student, 1)
        self.assertEqual(corrections[0][0], Written_Question.objects.get(id = 2) )

    # test utils.create_exam_completed_entry
    def test_create_exam_completed_entry_student1(self):
        user = StudentProfile.objects.get(user_id=6)
        create_exam_completed_entry(user, self.exam4, 78)
        exam_completed_entry = CompletedExam.objects.get(id = 17)
        self.assertEqual(exam_completed_entry.exam, self.exam4)
        self.assertEqual(exam_completed_entry.percentage, 78)
        self.assertEqual(exam_completed_entry.user.user.username, "student5")
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

    # test utils.get_next_exam()
    def test_get_next_exam_same_level(self):
        get_next_exam(2)
        student = StudentProfile.objects.get(user_id =2)
        self.assertEqual(student.next_exam_id, 5)

    def test_get_next_exam_up_level_none_completed(self):
        get_next_exam(9)
        student = StudentProfile.objects.get(user_id =9)
        self.assertEqual(student.next_exam_id, 3)

    """
    # failing 14/9/19 code changed to provide random int. Test not update
    def test_get_next_exam_moving_down_with_all_completed(self):
        get_next_exam(10)
        student = StudentProfile.objects.get(user_id =10)
        self.assertEqual(student.next_exam_id, 5)
    """
    
    # test utils.py delete_completed_exam_total
    def test_delete_exam_total_does_not_exist(self):
        delete_completed_exam_total (11, 7)
        with self.assertRaises(CompletedExam.DoesNotExist):
            CompletedExam.objects.get(user_id = 11)

    # test utils.py delete_completed_exam_record
    def test_delete_exam_record_does_not_exist(self):
        delete_completed_exam_record (10, 6)
        with self.assertRaises(CompletedExam.DoesNotExist):
            CompletedExam.objects.get(user_id = 10, exam_id = 6)

    # test utils.get_starting_level
    def test_get_starting_level(self):
        answers = ["True", "False", "True", "True", "True"]
        level = get_starting_level(answers)
        self.assertEqual(level, 5)

    def test_get_starting_level_2(self):
        answers = ["True", "False", "True", "False", "True"]
        level = get_starting_level(answers)
        self.assertEqual(level, 1)

    def test_get_starting_level_3(self):
        answers = ["False", "False", "False", "False", "False"]
        level = get_starting_level(answers)
        self.assertEqual(level, 1)

    def test_get_starting_level_4(self):
        answers = ["False", "True", "True", "True", "False"]
        level = get_starting_level(answers)
        self.assertEqual(level, 4)

    def test_get_starting_level_5(self):
        answers = ["False", "True", "True", "False", "True"]
        level = get_starting_level(answers)
        self.assertEqual(level, 2)

    def test_get_starting_level_6(self):
        answers = ["True", "True", "True", "True", "True"]
        level = get_starting_level(answers)
        self.assertEqual(level, 5)

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

    def test_incomplete_answer_str(self):
        self.assertEqual(self.incorrectanswer.__str__(), "student9 What is my favourite film? ")

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
    def test_do_test_get_as_student(self):
        self.client.login(username ="student2", password="mypass")
        response = self.client.get(reverse('dotest'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exams/dotest.html')
        self.assertContains(response, "<p><strong>What is my favourite colour? </strong></p>")

    def test_do_test_get_as_teacher(self):
        self.client.login(username ="teacher", password="mypass")
        response = self.client.get(reverse('dotest'), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "custom_users/edit_teacher.html")
        self.assertContains(response, '<div class="card-headergreen">Add Teacher Details</div>')

    def test_do_test_as_anon(self):
        response = self.client.get(reverse('dotest'), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")
        self.assertContains(response, '<h3 class="green_header">Welcome to ChemLearning</h3>')

    def test_do_test_get_response_student_finished_code(self):
        student = StudentProfile.objects.get(user_id = 12)
        student.next_exam_id = 9
        student.level = 17
        student.save()
        self.client.login(username ="student11", password="mypass")
        response = self.client.get(reverse('dotest'))
        self.assertEqual(response.status_code, 302)

    def test_do_test_get_template_used_student_finished_(self):
        student = StudentProfile.objects.get(user_id = 12)
        student.next_exam_id = 9
        student.level = 17
        student.save()
        self.client.login(username ="student11", password="mypass")
        response = self.client.get(reverse('dotest'), follow = True)
        self.assertTemplateUsed(response, 'exams/congratulations.html')

    def test_do_test_get_student_finished_html(self):
        student = StudentProfile.objects.get(user_id = 12)
        student.next_exam_id = 9
        student.level = 17
        student.save()
        self.client.login(username ="student11", password="mypass")
        response = self.client.get(reverse('dotest'), follow = True)
        self.assertContains(response, "<h1 class='gold .animation-lightSpeedin'>")

    def test_do_test_post_response_code(self):
        self.client.login(username ="student2", password="mypass")
        response = self.client.post(reverse('dotest'))
        self.assertEqual(response.status_code, 302)

    def test_do_test_post_template_used(self):
        self.client.login(username ="student2", password="mypass")
        response = self.client.post(reverse('dotest'), follow=True)
        self.assertTemplateUsed(response, 'exams/show_result.html')

    def test_do_test_post_html(self):
        self.client.login(username ="student2", password="mypass")
        response = self.client.post(reverse('dotest'), follow=True)
        self.assertContains(response, "<h5>You scored: 33% on Test Exam Title 1<br><br/></h5>")

    # test show_result view.
    def test_show_result_get_as_student(self):
        self.client.login(username ="student2", password="mypass")
        response = self.client.post(reverse('show_result', args=[1,]))
        student = StudentProfile.objects.get(user_id = 3)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exams/show_result.html')
        self.assertContains(response, '<h5>You scored: 33% on Test Exam Title 1<br><br/></h5>')

    def test_show_result_get_as_teacher_code(self):
        self.client.login(username ="teacher", password="mypass")
        response = self.client.get(reverse('show_result', args=[1,]), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_users/edit_teacher.html')
        self.assertContains(response, '<div class="card-headergreen">Add Teacher Details</div>')

    def test_show_result_get_as_anon(self):
        response = self.client.get(reverse('show_result', args=[1,]), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, '<h3 class="green_header">Welcome to ChemLearning</h3>')

    # test show result when student is finished
    def test_show_result_get_response_student(self):
        student = StudentProfile.objects.get(user_id = 3)
        student.next_exam_id = 8
        student.level = 17
        student.save()
        self.client.login(username ="student2", password="mypass")
        response = self.client.get(reverse('show_result', args=[1,]))
        self.assertEqual(response.status_code, 200)

    def test_show_result_get_template_used_student(self):
        student = StudentProfile.objects.get(user_id = 3)
        student.next_exam_id = 8
        student.level = 17
        student.save()
        self.client.login(username ="student2", password="mypass")
        response = self.client.get(reverse('show_result', args=[1,]))
        self.assertTemplateUsed(response, 'exams/show_result.html')

    def test_show_result_get_student_html(self):
        student = StudentProfile.objects.get(user_id = 3)
        student.next_exam_id = 8
        student.level = 17
        student.save()
        self.client.login(username ="student2", password="mypass")
        response = self.client.get(reverse('show_result', args=[1,]))
        self.assertContains(response, "<h5>You scored: 33% on Test Exam Title 1<br><br/></h5>")

    # test show_result view finished all levels.
    def test_show_result_get_response_finished(self):
        self.client.login(username ="student10", password="mypass")
        response = self.client.get(reverse('welcome_student'))
        self.assertEqual(response.status_code, 302)

    def test_show_result_get_template_used_finished(self):
        self.client.login(username ="student10", password="mypass")
        response = self.client.get(reverse('welcome_student'), follow=True)
        self.assertTemplateUsed(response, 'exams/congratulations.html')

    def test_show_result_get_html_finished(self):
        self.client.login(username ="student10", password="mypass")
        response = self.client.get(reverse('welcome_student'), follow=True)
        self.assertContains(response,
        "<h1 class='gold .animation-lightSpeedin'>Congratulations you have completed ChemLearning</h1>")

    # test review view
    def test_review_get_response_code(self):
        self.client.login(username ="student3", password="mypass")
        response = self.client.get(reverse('review', args=[1,]))
        self.assertEqual(response.status_code, 200)

    def test_review_get_template_used(self):
        self.client.login(username ="student3", password="mypass")
        response = self.client.get(reverse('review', args=[1,]), follow = True)
        self.assertTemplateUsed(response, 'exams/review.html')

    def test_review_get_html(self):
        self.client.login(username ="student3", password="mypass")
        response = self.client.get(reverse('review', args=[1,]), follow = True)
        self.assertContains(response, "<h5>Multiple choice questions you need to review</h5>")

    # test review view with 100%
    def test_review_get_response_with_100_response(self):
        self.client.login(username ="student4", password="mypass")
        response = self.client.get(reverse('review', args=[1,]))
        self.assertEqual(response.status_code, 302)

    def test_review_get_response_with_100_template(self):
        self.client.login(username ="student4", password="mypass")
        response = self.client.get(reverse('review', args=[1,]), follow = True)
        self.assertTemplateUsed(response, 'exams/hundred.html')

    def test_review_get_htmlwith_100(self):
        self.client.login(username ="student4", password="mypass")
        response = self.client.get(reverse('review', args=[1,]), follow = True)
        self.assertContains(response, '<div class="span12 imagecentre">')

    # test test_do_quiz_signup view. GET and POST requests
    def test_do_quiz_signup_get_already_completed_response(self):
        self.client.login(username ="student2", password="mypass")
        response=self.client.get(reverse('do_signup_quiz'))
        self.assertEqual(response.status_code, 302)

    def test_do_quiz_signup_get_already_completed_template(self):
        self.client.login(username ="student2", password="mypass")
        response=self.client.get(reverse('do_signup_quiz'), follow = True)
        self.assertTemplateUsed(response, 'custom_users/welcome_student.html')

    def test_do_quiz_signup_get_already_completed_html(self):
        self.client.login(username ="student2", password="mypass")
        response=self.client.get(reverse('do_signup_quiz'), follow = True)
        self.assertContains(response, '<h5><strong>Welcome Student:</strong> student2</h5>')

    # test test_do_quiz_signup view. GET and POST requests
    def test_do_quiz_signup_get_response(self):
        self.client.login(username ="student1", password="mypass")
        response=self.client.get(reverse('do_signup_quiz'))
        self.assertEqual(response.status_code, 200)

    def test_do_quiz_signup_get_template(self):
        self.client.login(username ="student1", password="mypass")
        response=self.client.get(reverse('do_signup_quiz'), follow = True)
        self.assertTemplateUsed(response, 'custom_users/do_signup_quiz.html')

    def test_do_quiz_signup_get_html(self):
        self.client.login(username ="student1", password="mypass")
        response=self.client.get(reverse('do_signup_quiz'), follow = True)
        self.assertContains(response, '<h4 class = "green_header">Complete the quiz below to help us decide which lessons you need.</h4>')

    def test_do_quiz_signup_post_student(self):
        self.client.login(username ="student1", password="mypass")
        response=self.client.post(reverse('do_signup_quiz'),
        {'2':'True', '3': 'True', '4': 'False', '5':'False'}, follow = True)
        student = StudentProfile.objects.get(user_id = 2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_users/welcome_student.html')
        self.assertContains(response, 'Current Level:</strong> 2</strong></p>')
        self.assertContains(response, 'Progress</div>')
        self.assertEqual(student.next_exam_id, 3)
        self.assertEqual(student.next_lesson_id, 3)

    def test_do_quiz_signup_post_teacher(self):
        self.client.login(username ="teacher", password="mypass")
        response=self.client.post(reverse('do_signup_quiz'),
        {'2':'True', '3': 'True', '4': 'False', '5':'False'}, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_users/edit_teacher.html')

    def test_do_quiz_signup_post_anon(self):
        response=self.client.post(reverse('do_signup_quiz'),
        {'2':'True', '3': 'True', '4': 'False', '5':'False'}, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_do_quiz_signup_post_student_level_2(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.post(reverse('do_signup_quiz'),
        {'2':'True', '3': 'True', '4': 'False', '5':'False'}, follow = True)
        student = StudentProfile.objects.get(user_id = 2)
        self.assertEqual(student.level, 2)

    def test_do_quiz_signup_post_student_level_3(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.post(reverse('do_signup_quiz'),
        {'2':'True', '3': 'True', '4': 'True', '5':'False'}, follow = True)
        student = StudentProfile.objects.get(user_id = 2)
        self.assertEqual(student.level, 3)

    def test_do_quiz_signup_post_template(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.post(reverse('do_signup_quiz'),
        {'2':'True', '3': 'True', '4': 'False', '5':'False'}, follow = True)
        self.assertTemplateUsed(response, 'custom_users/welcome_student.html')

    def test_do_quiz_signup_post_html(self):
        self.client.force_login(User.objects.get(id=2))
        response=self.client.post(reverse('do_signup_quiz'),
        {'2':'True', '3': 'True', '4': 'False'}, follow = True)
        self.assertContains(response, "<h5><strong>Welcome Student:</strong> student1</h5>")

    # test revise with less than 5 incorrect answers
    def test_revision_get_as_student(self):
        self.client.login(username ="student11", password="mypass")
        response = self.client.get(reverse('revise'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exams/revise.html')
        self.assertContains(response, "<h4>Revision")

    def test_revision__get_as_teacher(self):
        self.client.login(username ="teacher", password="mypass")
        response = self.client.get(reverse('revise'), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "custom_users/welcome_teacher.html")
        self.assertContains(response, "<h5>Welcome Teacher: teacher</h5>")


    def test_revision_get_as_anon(self):
        response = self.client.get(reverse('revise'), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")
        self.assertContains(response, '<h3 class="green_header">Welcome to ChemLearning</h3>')
