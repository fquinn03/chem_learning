from custom_users.models import Class_id
from exams.models import UserAnswer

"""
Get a user's answers to questions for the teacher to view
"""
def get_questions_and_student_answers(questions, student):
    question_and_answer = {}
    for question in questions:
        answer = UserAnswer.objects.get(question = question.id, user = student.user_id)
        question_and_answer[question] = answer
    return question_and_answer

"""
Create new class (teaching group) for teacher
"""
def create_new_class(form, teacher):
    class_name = form.cleaned_data['name']
    Class_id.objects.create(name = class_name, teacher = teacher)
