from django.db import transaction
from django.shortcuts import render
from custom_users.models import StudentProfile
from .models import Answer, Exam, Formula_Question, Level, MCQ_Question, Question, UserAnswer, Written_Question
from .utils import calculate_percentage, create_user_answer, get_corrections_formula, get_corrections_mcq, get_corrections_written, get_formula

"""Use the exam_id to get all the questions for the exam. If GET request display the questions and answer options.
If POST request, use utils.create_user_answer to add a user_answer to the database for each question answered
and then display finish_test template"""
def dotest(request, exam_id):
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.filter(exam = exam_id)
    written_questions = Written_Question.objects.filter(exam = exam_id)
    mcq_questions = MCQ_Question.objects.filter(exam = exam_id)
    formula_questions = Formula_Question.objects.filter(exam = exam_id)
    if request.method == 'POST':
        with transaction.atomic():
            create_user_answer(request.POST, StudentProfile.objects.get(user_id = request.user.id) )
            return render(request, 'exams/finish_test.html', {
                'exam': exam,
                })
    else:
        return render(request, 'exams/dotest.html', {
            'mcq_questions': mcq_questions, 'written_questions':written_questions, 'formula_questions':formula_questions,
            'questions': questions
})

""" Use the exam_id to get all the questions for the exam.  Use utils.calculate_percentage to
check if the user_answer in the database for each question is correct, calculate the user's
percentage result and then display show_result template  """
def show_result(request, exam_id):
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    percentage_result = calculate_percentage(questions, request.user.id, exam_id)
    return render(request, 'exams/show_result.html', {'percentage_result': percentage_result,
    'exam':exam,
    })

""" Use the exam_id to get all the questions for the exam.  Use utils.test_get_corrections to add
check if the user_answer in the database for each question is correct, calculate the user's result
and then display show_result template  """
def review(request, exam_id):
    mcq_corrections = get_corrections_mcq(request.user.id, exam_id)
    written_corrections = get_corrections_written(request.user.id, exam_id)
    written_corrections_incorrect = written_corrections[0]
    written_corrections_mispelled = written_corrections[1]
    formula_corrections = get_corrections_formula(request.user.id, exam_id)
    mispelled_count = len(written_corrections_mispelled)
    formulae_count = len(formula_corrections)
    return render(request, 'exams/review.html', {'mcq_corrections': mcq_corrections, 'written_corrections_incorrect':
    written_corrections_incorrect, 'written_corrections_mispelled':written_corrections_mispelled,
    'formula_corrections':formula_corrections, 'mispelled_count':mispelled_count, 'formulae_count':formulae_count
})
