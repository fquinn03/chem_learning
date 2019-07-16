from django.shortcuts import render
from .models import Answer, Exam, UserAnswer, Question, Level


def dotest(request, exam_id, q_no):
    number_of_q = Question.objects.all(exam_id).count()
    question = Question.objects.get(exam = exam_id, number = q_no)
    answers = Answer.objects.all().filter(question = question)
    return render(request, 'exams/dotest.html', {
        'question': question,
        'answers': answers,
    })
