from chempy import Substance
from custom_users.models import Class_id, StudentProfile, TeacherProfile
from .models import Answer, Exam, Formula_Question, Level, MCQ_Question, Question, UserAnswer, Written_Question

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
def calculate_percentage(questions, user_id, exam_id):
    total_questions = questions.count()
    mcq_questions = MCQ_Question.objects.filter(exam_id = exam_id)
    written_questions = Written_Question.objects.filter(exam_id = exam_id)
    formula_questions = Formula_Question.objects.filter(exam_id = exam_id)
    right = 0
    for question in mcq_questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        correct_answers =  Answer.objects.filter(question = question.id, correct=True)
        for answer in correct_answers:
            if student_answer.user_answer == answer.text:
                right +=1

    for question in written_questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        correct_answers =  Answer.objects.filter(question = question.id, correct=True)
        for answer in correct_answers:
            if student_answer.user_answer.lower().strip() == answer.text.lower():
                right +=1

    for question in formula_questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        correct_answers =  Answer.objects.filter(question = question.id, correct=True)
        for answer in correct_answers:
            if student_answer.user_answer == answer.text:
                right +=1
    percentage_result = round((right/total_questions)*100)
    return percentage_result

""" Iterate through each question in the submitted test and check if the users_answer is correct. If correct but incorrectly mispelled
    add the correct spelling to the review item. If incorrect add correct answer to reveiw object corrections and display through review template  """
def get_corrections_mcq(user_id, exam_id):
    mcq_questions = MCQ_Question.objects.filter(exam = exam_id)
    mcq_corrections = {}
    for question in mcq_questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        correct_answer =  Answer.objects.get(question = question.id, correct=True, correct_spelling = True)
        if student_answer.user_answer != correct_answer.text:
            mcq_corrections[question.text] = correct_answer.text
    return mcq_corrections

def get_corrections_written(user_id, exam_id):
    written_questions = Written_Question.objects.filter(exam = exam_id)
    written_corrections = {}
    mispelled = {}
    acceptable_answers =[]
    for question in written_questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        correct_answer =  Answer.objects.get(question = question.id, correct=True, correct_spelling = True)
        possible_answers =  Answer.objects.filter(question = question.id, correct=True, correct_spelling = False)
        for possible_answer in possible_answers:
            acceptable_answers.append(possible_answer.text.lower())
        if student_answer.user_answer != correct_answer.text:
            if student_answer.user_answer.lower().strip() in acceptable_answers:
                mispelled[question.text] = correct_answer.text
            else:
                written_corrections[question.text] = correct_answer.text

    return (written_corrections, mispelled)

def get_corrections_formula(user_id, exam_id):
    formula_questions = Formula_Question.objects.filter(exam = exam_id)
    formula_corrections = {}
    for question in formula_questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        correct_answer =  Answer.objects.get(question = question.id, correct=True, correct_spelling = True)
        if student_answer.user_answer != correct_answer.text:
            formula_corrections[question.text] = get_formula(correct_answer.text)
    return formula_corrections


""" Convert a string chemical formula to HTML chemical formula for rendering """
def get_formula(raw_formula):
    formula = Substance.from_formula(raw_formula)
    html_formula = formula.html_name
    return html_formula
