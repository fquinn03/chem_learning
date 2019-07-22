from django.shortcuts import render
from .models import Answer, Exam, UserAnswer, Question, Level
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import QuestionForm


def dotest(request, exam_id):
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    form = QuestionForm(request.POST)
    if request.method == 'POST':
        print(request.POST)
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                q = Question.objects.get(id = key)
                a = Answer.objects.get(id = value)
                print("Question "+q.text +" Answer: "+ a.text)
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
