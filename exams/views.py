from .models import Answer, Exam, UserAnswer, Question, Level
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from users.models import StudentProfile
from .utils import calculate_percentage, create_user_answer, get_corrections

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

def show_result(request, exam_id):
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    percentage_result = calculate_percentage(questions, request.user.id)
    return render(request, 'exams/show_result.html', {'percentage_result': percentage_result,
    'exam':exam,
    })

def review(request, exam_id):
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    corrections = get_corrections(questions, request.user.id)
    return render(request, 'exams/review.html', {'corrections': corrections})
