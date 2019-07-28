from users.models import Class_id, User, StudentProfile, TeacherProfile
from .models import Level, Exam, Question, Answer, UserAnswer

""" Iterate through each question in the submitted test and store the user's answer in the database  """
def create_user_answer(post_request, user):
    for key, value in post_request.items():
        if key != 'csrfmiddlewaretoken':
            q = Question.objects.get(id = key)
            u = user
            useranswer = UserAnswer.objects.create(question = q, user_answer = value, user = u)
            useranswer.save()

""" Iterate through each question in the submitted test and check if the users_answer is correct to work out their percentage_result
for the test  """
def calculate_percentage(questions, user_id):
    total_questions = questions.count()
    right = 0
    for question in questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        correct_answer =  Answer.objects.get(question = question.id, correct=True)
        if student_answer.user_answer.lower() == correct_answer.text.lower():
            right +=1
    percentage_result = round((right/total_questions)*100)
    return percentage_result

""" Iterate through each question in the submitted test and check if the users_answer is correct. If not add the question and review.text
 to corrections and display through review template  """
def get_corrections(questions, user_id):
    corrections = {}
    for question in questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        correct_answer =  Answer.objects.get(question = question.id, correct=True)
        if student_answer.user_answer.lower() != correct_answer.text.lower():
            corrections[question.text] = correct_answer.text
    return corrections
