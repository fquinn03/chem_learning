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
