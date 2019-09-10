from custom_users.models import Class_id
from exams.models import UserAnswer

"""
Returns a dictionary containing the questions in a quiz as the keys
and a student's answers to those questions as the values
"""
def get_questions_and_student_answers(questions, student):
    question_and_answer = {}
    for question in questions:
        answer = UserAnswer.objects.get(question = question.id, user = student.user_id)
        question_and_answer[question] = answer
    return question_and_answer

"""
Creates new class (teaching group) for a teacher
"""
def create_new_class(form, teacher):
    class_name = form.cleaned_data['name']
    Class_id.objects.create(name = class_name, teacher = teacher)
