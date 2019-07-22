from django.shortcuts import render
from .models import Answer, Exam, UserAnswer, Question, Level
from users.models import StudentProfile
from django.http import HttpResponseRedirect
from django.shortcuts import render



def dotest(request, exam_id):
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    if request.method == 'POST':
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
        print(request.GET)
        return render(request, 'exams/dotest.html', {
            'questions': questions,

    })
