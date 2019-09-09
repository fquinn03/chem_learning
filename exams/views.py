from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from custom_users.models import StudentProfile
from custom_users.utils import (user_is_student, have_student_details,
have_student_signup, is_finished, sign_up_quiz_already_completed)
from .models import (Exam, CompletedExam, IncorrectAnswer, Formula_Question,
MCQ_Question, Question, Written_Question)
from .utils import (calculate_percentage, create_exam_completed_entry, create_user_answer,
delete_completed_exam_record, delete_completed_exam_total, get_corrections_formula, get_corrections_mcq,
get_corrections_written, get_level, get_next_exam, get_next_lesson, get_revision_resources,
get_starting_level)

"""
Use the exam_id to get all the questions for the exam. If GET request display the questions
and answer options.If POST request, use utils.create_user_answer to add a user_answer to
the database for each question answered and then display finish_test template
"""
@login_required
@user_passes_test(user_is_student, login_url = 'welcome_teacher')
@user_passes_test(have_student_details, login_url = 'edit_student',  redirect_field_name = 'get_student_details' )
@user_passes_test(have_student_signup,  login_url = 'do_signup_quiz', redirect_field_name = 'do_signup_quiz')
def dotest(request):
    student = StudentProfile.objects.get(user_id = request.user.id)
    #if the student has previously completed this exam delete the record
    delete_completed_exam_total(student, student.next_exam_id)
    try:
        # if a student does not have a next_exam_id they have finished the course
        exam = Exam.objects.get(id = student.next_exam_id)
        # get all the questions in the exam
        questions = Question.objects.filter(exam = student.next_exam_id)
        # the types of question get more challenging from start to end of test
        mcq_questions = MCQ_Question.objects.filter(exam = student.next_exam_id)
        written_questions = Written_Question.objects.filter(exam = student.next_exam_id)
        formula_questions = Formula_Question.objects.filter(exam = student.next_exam_id)
        if request.method == 'POST':
            #create a record of the students answer
            create_user_answer(request.POST, StudentProfile.objects.get(user_id = request.user.id))
            return redirect('show_result', exam_id = exam.id)
        else:
            #if GET request show the questions and answer options/input
            return render(request, 'exams/dotest.html', {
                'mcq_questions': mcq_questions, 'written_questions':written_questions,
                'formula_questions':formula_questions,
                'questions': questions,
                'exam':exam
            })
    # the student has completed all the levels and does not have a next_exam_id
    except Exam.DoesNotExist:
        return redirect('congratulations')


"""
On signup a student user will complete this short quiz. This is the basis to assign their starting level.
If GET request the questions and answer options are displayed.
If POST request, go through the answers, assign student level and changed signup_quiz_completed flag
for student profile.
"""
@login_required
@user_passes_test(user_is_student, login_url = 'welcome_teacher')
@user_passes_test(have_student_details, login_url = 'edit_student',  redirect_field_name = 'get_student_details' )
@user_passes_test(sign_up_quiz_already_completed, login_url = 'welcome_student')
def do_signup_quiz(request):
    exam = Exam.objects.get(title = "signup_quiz")
    questions = Question.objects.filter(exam = exam.id)
    answers = []
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                answers.append(value)
        level = get_starting_level(answers)
        student = StudentProfile.objects.get(user_id = request.user.id)
        student.level = level
        student.signup_quiz_completed = True
        student.save()
        get_next_lesson(student.user_id)
        get_next_exam(student.user_id)
        return redirect('welcome_student')
    else:
        return render(request, 'custom_users/do_signup_quiz.html', {'questions': questions
        })

"""
Use the exam_id to get all the questions for the exam.  Use utils.calculate_percentage to
check if the user_answer in the database for each question is correct, calculate the user's
percentage result and then display show_result template.
"""
@login_required
@user_passes_test(user_is_student, login_url = 'welcome_teacher')
@user_passes_test(have_student_details, login_url = 'edit_student',  redirect_field_name = 'get_student_details' )
@user_passes_test(have_student_signup,  login_url = 'do_signup_quiz', redirect_field_name = 'do_signup_quiz')
def show_result(request, exam_id):
    student = StudentProfile.objects.get(user_id = request.user.id)
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    percentage_result = calculate_percentage(questions, request.user.id, exam_id)
    delete_completed_exam_record(student, exam_id)
    create_exam_completed_entry(student, exam, percentage_result)
    get_level(request.user.id)
    try:
        get_next_exam(request.user.id)
        get_next_lesson(request.user.id)
        return render(request, 'exams/show_result.html', {'percentage_result': percentage_result,
        'exam':exam,
        })
    except IndexError:
        return render(request, 'exams/show_result.html', {'percentage_result': percentage_result,
        'exam':exam,
        })

"""
Use the exam_id to get all the questions for the exam.  Check the student's percentage for the exam.
If 100 just show 100% congratulations image
Else  go through their answers and use the utils.get_corrections_mcq, get_corrections_written, get_corrections_formula
functions and show the student their corrections
"""
@login_required
@user_passes_test(user_is_student, login_url = 'welcome_teacher')
@user_passes_test(have_student_details, login_url = 'edit_student',  redirect_field_name = 'get_student_details' )
@user_passes_test(have_student_signup,  login_url = 'do_signup_quiz', redirect_field_name = 'do_signup_quiz')
def review(request, exam_id):
    student = StudentProfile.objects.get(user_id = request.user.id)
    exam = CompletedExam.objects.get(user_id = request.user.id, exam = exam_id)
    if exam.percentage == 100:
        return redirect('hundred')
    else:
        mcq_corrections = get_corrections_mcq(request.user.id, exam_id)
        written_corrections = get_corrections_written(request.user.id, exam_id)
        written_corrections_incorrect = written_corrections[0]
        written_corrections_mispelled = written_corrections[1]
        formula_corrections = get_corrections_formula(request.user.id, exam_id)
        mispelled_count = len(written_corrections_mispelled)
        formulae_count = len(formula_corrections)
        return render(request, 'exams/review.html', {'mcq_corrections': mcq_corrections,
        'written_corrections_incorrect': written_corrections_incorrect,
        'written_corrections_mispelled':written_corrections_mispelled,
        'formula_corrections':formula_corrections, 'mispelled_count':mispelled_count,
        'formulae_count':formulae_count
        })

"""
When the student clicks on revision button on the welcome page
Display their tailored revision resources chosen from questions they
have answered incorrectly
"""
@login_required
@user_passes_test(user_is_student)
@user_passes_test(have_student_details, login_url = 'edit_student',  redirect_field_name = 'get_student_details' )
@user_passes_test(have_student_signup,  login_url = 'do_signup_quiz', redirect_field_name = 'do_signup_quiz')
def revise(request):
    revision_resources = get_revision_resources(request.user.id)
    incorrect_questions = revision_resources[0]
    number_of_q = revision_resources[1]
    return render(request, 'exams/revise.html', {
    'incorrect_questions':incorrect_questions,
    'number_of_q':number_of_q
    })

@login_required
@user_passes_test(user_is_student)
@user_passes_test(is_finished)
def congratulations(request):
    return render(request, 'exams/congratulations.html')

@login_required
@user_passes_test(user_is_student)
def hundred(request):
    return render(request, 'exams/hundred.html')
