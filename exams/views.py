from django.shortcuts import render
from .models import Answer, Exam, UserAnswer, Question, Level
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import QuestionForm, AnswerForm


def dotest(request, exam_id):
    questions = Question.objects.all().filter(exam = exam_id)
    return render(request, 'exams/dotest.html', {
        'questions': questions,

    })
