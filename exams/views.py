from .models import Answer, Exam, UserAnswer, Question, Level
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from users.models import StudentProfile

def dotest(request, exam_id):
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    if request.method == 'POST':
        with transaction.atomic():
            for key, value in request.POST.items():
                if key != 'csrfmiddlewaretoken':
                    q = Question.objects.get(id = key)
                    a = Answer.objects.get(id = value)
                    u = StudentProfile.objects.get(user_id = request.user.id)
                    useranswer = UserAnswer(question = q, user_answer = a, user = u)
                    useranswer.save()
                else:
                    continue
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
    total_questions = questions.count()
    right = 0
    for question in questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = request.user.id)
        if student_answer.user_answer == Answer.objects.get(question = question.id, correct =True):
            right +=1
    percentage_result = round((right/total_questions)*100)

    return render(request, 'exams/show_result.html', {'percentage_result': percentage_result,
    'exam':exam,
    })
