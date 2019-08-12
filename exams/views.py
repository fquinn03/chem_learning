from django.db import transaction
from django.shortcuts import render, redirect
from custom_users.models import StudentProfile
from .models import (Answer, Exam, CompletedExam, Formula_Question,
MCQ_Question, Question, UserAnswer, Written_Question)
from .utils import (calculate_percentage, create_exam_completed_entry, create_user_answer,
get_corrections_formula, get_corrections_mcq, get_corrections_written, get_formula,
get_level)
"""
Use the exam_id to get all the questions for the exam. If GET request display the questions
and answer options.If POST request, use utils.create_user_answer to add a user_answer to
the database for each question answered and then display finish_test template
"""
def dotest(request, exam_id):
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.get(user_id = request.user.id)
            if student.details_added and student.signup_quiz_completed:
                exam = Exam.objects.get(id = exam_id)
                if exam.id == student.next_exam_id and exam.level == student.level:
                    questions = Question.objects.filter(exam = exam_id)
                    written_questions = Written_Question.objects.filter(exam = exam_id)
                    mcq_questions = MCQ_Question.objects.filter(exam = exam_id)
                    formula_questions = Formula_Question.objects.filter(exam = exam_id)
                    if request.method == 'POST':
                        with transaction.atomic():
                            create_user_answer(request.POST, StudentProfile.objects.get(user_id = request.user.id) )
                        return redirect('show_result', exam_id = exam.id)
                    else:
                        return render(request, 'exams/dotest.html', {
                            'mcq_questions': mcq_questions, 'written_questions':written_questions,
                            'formula_questions':formula_questions,
                            'questions': questions
                        })
                else:
                    return redirect('welcome_student')

            elif student.details_added:
                return redirect('do_signup_quiz')
            else:
                return redirect('edit_student')
        except:
            return redirect('home')
    else:
        return redirect('signup')

"""
On signup a student user will complete this short quiz. This is the basis to assign their starting level.
If GET request the questions and answer options are displayed.
If POST request, go through the answers, assign student level and changed signup_quiz_completed flag
for student profile.
"""
def do_signup_quiz(request):
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.get(user_id = request.user.id)
            if student.details_added and student.signup_quiz_completed:
                return redirect('welcome_student')
            elif student.details_added:
                exam = Exam.objects.get(title = "signup_quiz")
                questions = Question.objects.filter(exam = exam.id)
                answers = []
                level = 1
                if request.method == 'POST':
                    for key, value in request.POST.items():
                        if key != 'csrfmiddlewaretoken':
                            answers.append(value)

                    for i in range(len(answers)):
                        if answers[i] == "True":
                            level = i+1
                    student = StudentProfile.objects.get(user_id = request.user.id)
                    student.level = level
                    student.signup_quiz_completed = True
                    student.save()
                    return redirect('welcome_student')
                else:
                    return render(request, 'custom_users/do_signup_quiz.html', {'questions': questions
                    })
            else:
                return rediect('edit_student')
        except:
            return redirect('home')
    else:
        return redirect('signup')


"""
Use the exam_id to get all the questions for the exam.  Use utils.calculate_percentage to
check if the user_answer in the database for each question is correct, calculate the user's
percentage result and then display show_result template.
"""
def show_result(request, exam_id):
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.get(user_id = request.user.id)
            if student.details_added and student.signup_quiz_completed:
                exam = Exam.objects.get(id = exam_id)
                questions = Question.objects.all().filter(exam = exam_id)
                percentage_result = calculate_percentage(questions, request.user.id, exam_id)
                create_exam_completed_entry(student, exam, percentage_result)
                get_level(request.user.id)
                return render(request, 'exams/show_result.html', {'percentage_result': percentage_result,
                'exam':exam,
                })
            elif student.details_added:
                return redirect('do_signup_quiz')
            else:
                return redirect('edit_student')
        except:
            return redirect('home')
    else:
        return redirect('signup')

"""
Use the exam_id to get all the questions for the exam.  Use utils.test_get_corrections to add
check if the user_answer in the database for each question is correct, calculate the user's result
and then display show_result template.
"""
def review(request, exam_id):
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.get(user_id = request.user.id)
            if student.details_added and student.signup_quiz_completed:
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
            elif student.details_added:
                return redirect('do_signup_quiz')
            else:
                return redirect('edit_student')
        except:
            return redirect('home')
    else:
        return redirect('signup')
