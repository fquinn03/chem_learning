from .models import Level, Exam, Question, Answer, UserAnswer
from users.models import Class_id, User, StudentProfile, TeacherProfile

def create_user_answer(post_request, user):
    for key, value in post_request.items():
        if key != 'csrfmiddlewaretoken':
            q = Question.objects.get(id = key)
            a = Answer.objects.get(id = value)
            u = user
            useranswer = UserAnswer.objects.create(question = q, user_answer = a, user = u)
            useranswer.save()
        else:
            continue

def calculate_percentage(questions, user_id):
    total_questions = questions.count()
    right = 0
    for question in questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        if student_answer.user_answer == Answer.objects.get(question = question.id, correct=True):
            right +=1
    percentage_result = round((right/total_questions)*100)
    return percentage_result

def get_corrections(questions, user_id):
    corrections = {}
    for question in questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        if student_answer.user_answer != Answer.objects.get(question = question.id, correct=True):
            corrections[question.text] = Answer.objects.get(question = question.id, correct=True)
    return corrections
