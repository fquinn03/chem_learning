from chempy import Substance
from django.db import transaction
from django.shortcuts import render
from users.models import StudentProfile
from .models import Answer, Exam, UserAnswer, Question, Level
from .utils import calculate_percentage, create_user_answer, get_corrections

"""Use the exam_id to get all the questions for the exam. If GET request display the questions and answer options.
If POST request, use utils.create_user_answer to add a user_answer to the database for each question answered
and then display finish_test template"""
def dotest(request, exam_id):
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    if request.method == 'POST':
        with transaction.atomic():
            create_user_answer(request.POST, StudentProfile.objects.get(user_id = request.user.id) )
            return render(request, 'exams/finish_test.html', {
                'exam': exam,
                })
    else:
        return render(request, 'exams/dotest.html', {
            'questions': questions,
})

""" Use the exam_id to get all the questions for the exam.  Use utils.calculate_percentage to
check if the user_answer in the database for each question is correct, calculate the user's
percentage result and then display show_result template  """
def show_result(request, exam_id):
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    percentage_result = calculate_percentage(questions, request.user.id)
    return render(request, 'exams/show_result.html', {'percentage_result': percentage_result,
    'exam':exam,
    })

""" Use the exam_id to get all the questions for the exam.  Use utils.test_get_corrections to add
check if the user_answer in the database for each question is correct, calculate the user's result
and then display show_result template  """
def review(request, exam_id):
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    incorrect = get_corrections(questions, request.user.id)
    corrections = incorrect[0]
    mispelled = incorrect[1]
    mispelled_count = len(mispelled)
    return render(request, 'exams/review.html', {'corrections': corrections, 'mispelled':
    mispelled, 'mispelled_count':mispelled_count})

def get_formula(request, raw_formula):
    print(request)
    html_formula = Substance.from_formula(raw_formula)
    return render(request, 'dotest.html', {'html_formula':html_formula})
