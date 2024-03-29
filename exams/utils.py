from random import shuffle, randint
from chempy import Substance
from django.contrib.auth.models import User
from custom_users.models import Class_id, StudentProfile, TeacherProfile, User
from .models import (Answer, CompletedExam, Exam, Formula_Question,
MCQ_Question, IncorrectAnswer, Question, UserAnswer, Written_Question)
from lessons.models import Lesson

"""
Iterate through each question in the submitted test and create a UserAnswer in the database
"""
def create_user_answer(post_request, user):
    for key, value in post_request.items():
        if key != 'csrfmiddlewaretoken':
            q = Question.objects.get(id = key)
            u = user
            useranswer = UserAnswer.objects.create(question = q, user_answer = value, user = u)
            useranswer.save()

"""
Iterate through each type of question in the submitted test and check if the users_answer
is correct to work out their percentage_result for the test.
"""
def calculate_percentage(questions, user_id, exam_id):
    user = User.objects.get(id = user_id)
    total_questions = questions.count()
    #select each question type
    mcq_questions = MCQ_Question.objects.filter(exam = exam_id)
    written_questions = Written_Question.objects.filter(exam = exam_id)
    formula_questions = Formula_Question.objects.filter(exam = exam_id)
    right = 0
    #mark each question in each category
    for question in mcq_questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        correct_answers =  Answer.objects.filter(question = question.id).filter(correct=True)
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

    # calculate and return percentage
    percentage_result = round((right/total_questions)*100)
    return percentage_result

"""
Iterate through each MCQ question in the submitted test and check if the student's answer is correct.
If incorrect add question and correct answer to mcq_corrections dictionary
"""
def get_corrections_mcq(user_id, exam_id):
    student = StudentProfile.objects.get(user_id = user_id)
    mcq_questions = MCQ_Question.objects.filter(exam = exam_id) #Get all the MCQ questions on the exam
    mcq_corrections = []
    for question in mcq_questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id) # get the student's answer
        correct_answer =  Answer.objects.get(question = question.id, correct=True, correct_spelling = True)# get the correct answer
        if student_answer.user_answer != correct_answer.text: # compare answers and if incorrect
            mcq_corrections.append(question)  # add to mcq_corrections dictionary
            try:
                # check if this IncorrectAnswer has already been saved for revision for this student
                IncorrectAnswer.objects.get(question = question, user = student)
            except IncorrectAnswer.DoesNotExist:
                # create a record of the IncorrectAnswer for revision
                IncorrectAnswer.objects.create(question = question, user = student)
    return mcq_corrections

"""
Iterate through each Written question in the submitted test and check if the student's answer is correct.
For many written questions there are a number of acceptable answers e.g 100, hundred, a hundred
If incorrect add question and correct answer to written_corrections dictionary
If correct but mispelled add question and correct spelling to mispelled dictionary
"""
# correct Written style questions
def get_corrections_written(user_id, exam_id):
    student = StudentProfile.objects.get(user_id = user_id)
    written_questions = Written_Question.objects.filter(exam = exam_id) # get all the written questions on the exam.
    written_corrections = []
    mispelled = {}
    acceptable_answers =[]
    for question in written_questions:
        # get the student's answer
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id)
        # get any corrects, there may be more than one
        correct_answers =  Answer.objects.filter(question = question.id, correct=True, correct_spelling = True)
        #since there are many possible answers, this is the correct one to display in the review page
        correct_answer_to_display = Answer.objects.get(question = question.id, correct_answer_to_display = True )
        # get any acceptable mispelled answers
        possible_answers =  Answer.objects.filter(question = question.id, correct=True, correct_spelling = False)
        for possible_answer in possible_answers:
            acceptable_answers.append(possible_answer.text.lower()) # get a list of all acceptable mispelled answers
        correct_answer_found = False
        for correct_answer in correct_answers:
            # if the student's answer matches any of the acceptable correct answers the student is correct
            if student_answer.user_answer.lower().strip() == correct_answer.text.lower():
                correct_answer_found = True
        # check if the student's answer is correct but mispelled
        if not correct_answer_found:
            if student_answer.user_answer.lower().strip() in acceptable_answers:
                #add the correct spelling to the review items
                mispelled[question.text] = correct_answer.text
            else:
                # student answer is incorrect
                written_corrections.append(question)
                try:
                    # check if this IncorrectAnswer has already been saved for revision for this student
                    IncorrectAnswer.objects.get(question = question, user = student)
                except IncorrectAnswer.DoesNotExist:
                    # create a record of the IncorrectAnswer for revision
                    IncorrectAnswer.objects.create(question = question, user = student)
    return (written_corrections, mispelled)

"""
Iterate through each Formula_Question in the submitted test and check if the student's answer is correct.
If incorrect add question and correct answer to the formula_corrections dictionary
the correct_answer.text must be converted to HTML using the get_formula function
so that it is displayed correctly in the review page
"""
def get_corrections_formula(user_id, exam_id):
    student = StudentProfile.objects.get(user_id = user_id)
    formula_questions = Formula_Question.objects.filter(exam = exam_id) #Get all the Formula questions on the exam
    formula_corrections = {}
    for question in formula_questions:
        student_answer = UserAnswer.objects.get(question = question.id, user = user_id) # get user answer
        correct_answer =  Answer.objects.get(question = question.id, correct=True, correct_spelling = True) #get correct answer
        if student_answer.user_answer != correct_answer.text:
            formula_corrections[question.text] = get_formula(correct_answer.text) #if user answer not correct add to formula_corrections
            try:
                IncorrectAnswer.objects.get(question = question, user = student)
            except IncorrectAnswer.DoesNotExist:
                IncorrectAnswer.objects.create(question = question, user = student)
    return formula_corrections


"""
Convert a string chemical formula to HTML chemical formula to display on webpage.
"""
def get_formula(raw_formula):
    #use ChemPy to convert string raw_formula to chemical formula
    formula = Substance.from_formula(raw_formula)
    #use ChemPy to give html for formula eg H<sub>2</sub>O
    html_formula = formula.html_name
    return html_formula

"""
Method to record that a user has taken a particular exam.
Once a user completes an exam through the dotest view
an entry with their percentage is created in the CompletedExams table.
"""

def create_exam_completed_entry(user, exam, result):
    CompletedExam.objects.create(user = user, exam = exam, level = exam.level, percentage = result)



"""
Method to calculate a users score for a given level.  The method finds all the exams the user has taken
in that level. Calculates a weighted mean as the user's score for that level.
If the score is > 80% the level is incremented and attempts at this new level is reset to zero.
If the score is < 80% and the user has completed 3 exams at this level the level is decremented
and their attempt at this new level is reset to zero.
Otherwise the user stays on the same level and their attempts at this level is incremented.
"""
def get_level(user_id):
    student = StudentProfile.objects.get(user_id = user_id)
    level = student.level
    # get the exams the student has completed
    results = get_all_exam_results_for_level(student)
    # calculate a weighted mean for the exams completed
    weighted_mean = get_weighted_mean(results)
    # adjust level/attempts according to the weighted_mean
    adjust_level_and_attempts(student, weighted_mean)


"""
Find the next lesson for a student and link to it from the welcome student screen.
Get the students current level. Find the next lesson object for that level.
"""
def get_next_lesson(user):
    student = StudentProfile.objects.get(user_id = user)
    all_lessons = Lesson.objects.filter(level = student.level)
    completed_lessons = student.completed_lessons.filter(level = student.level)
    if len(completed_lessons) == len(all_lessons):
        for lesson in completed_lessons:
            student.completed_lessons.remove(lesson)
        next_lesson = all_lessons[0]
    else:
        for lesson in all_lessons:
            if lesson not in completed_lessons:
                next_lesson = lesson
                break
    student.next_lesson_id = next_lesson.id
    student.save()


"""
Find the next exam for a student and link to it from the welcome student screen.
Get the students current level. Find the next lesson object for that level.
"""
def get_next_exam(user):
    student = StudentProfile.objects.get(user_id = user)
    all_exam_ids = get_all_available_exam_ids(student)
    all_completed_exam_ids = get_all_completed_exam_ids(student)
    remaining_exams = get_remaining_exams(all_exam_ids, all_completed_exam_ids)
    if len(remaining_exams) == 0:
        x = random_num(len(all_exam_ids))
        next_exam = all_exam_ids[x]
    else:
        next_exam = remaining_exams[0]
    student.next_exam_id = next_exam
    student.save()

"""
Generate a random number between 0 and the number of exams
"""
def random_num(num_of_quizzes):
    x = randint(0, num_of_quizzes)
    return x

"""
Get a list of all a stuent's percentage quiz results at thier
current level.
"""
def get_all_exam_results_for_level(student):
    completed_exams = CompletedExam.objects.filter(level = student.level).filter(user = student)
    results = []
    # get a list of results for the exams completed
    for exam in completed_exams:
        results.append(exam.percentage)
    return results

"""
Calculate the weighted mean of a student's last two most recent quizes
if they are available or just return their only percentage.
"""
def get_weighted_mean(results):
    if len(results) == 0:
        weighted_mean = -1
    elif len(results) == 1:
        weighted_mean = results[0] * 1
    elif len(results) == 2:
        weighted_mean = results[1]*0.8 + results[0]*0.2
    else:
        weighted_mean = results[len(results)-1]*0.8 + results[len(results)-2]*0.2
    return weighted_mean

"""
Use the weighted mean to adjust the student's
level, attempts, progress and needs_help
This is the basis of the adaptive element of the application
"""
def adjust_level_and_attempts(student, weighted_mean):
    if weighted_mean >= 80:
        student.level += 1
        student.attempt = 0
        student.progress = 1
        student.needs_help = False

    elif weighted_mean == -1:
        student.attempt = 0
        student.progress = 2
        student.needs_help = False

    elif weighted_mean < 80 and student.attempt >= 3:
        if student.level > 1:
            student.level -= 1
            student.attempt = 0
            student.progress = 3
            student.needs_help = True
        else:
            student.level = 1
            student.attempt = 0
            student.progress = 2
            student.needs_help = True
    else:
        student.attempt += 1
        student.progress = 2
        student.needs_help = False

    student.save()

"""
Get all the exams a student could possible do at this level
"""
def get_all_available_exam_ids(student):
    all_exams = Exam.objects.filter(level = student.level)
    all_exam_ids = []
    for exam in all_exams:
        all_exam_ids.append(exam.id)
    return all_exam_ids


"""
Get all the exams a student has already done at this level
"""
def get_all_completed_exam_ids(student):
    completed_exams = CompletedExam.objects.select_related().filter(user = student).filter(level = student.level)
    all_completed_exam_ids = []
    for exam in completed_exams:
        all_completed_exam_ids.append(exam.exam.id)
    return all_completed_exam_ids

"""
Get all the exams a student has yet to do at this level
"""
def get_remaining_exams(all_exam_ids, all_completed_exam_ids):
    remaining_exams = []
    for id in all_exam_ids:
        if id not in all_completed_exam_ids:
            remaining_exams.append(id)
    return remaining_exams

"""
If a student has completed the same test already.
Delete the CompltedExam record and
their UserAnswer for each question
"""
def delete_completed_exam_total(student, exam_id):
    try:
        CompletedExam.objects.get(user = student, exam = exam_id).delete()
        questions = Question.objects.filter(exam = exam_id)
        for question in questions:
            UserAnswer.objects.get(user = student, question = question).delete()
    except CompletedExam.DoesNotExist:
        pass

"""
Deletes the completed exam record and creates a new one when the Teacher
clicks on a students quiz to see their answers.
If this didn't happen there is an error as the database contains multiple
copies of a students CompltedExam records
"""
def delete_completed_exam_record(student, exam_id):
    try:
        CompletedExam.objects.get(user = student, exam = exam_id).delete()
        questions = Question.objects.filter(exam = exam_id)
    except CompletedExam.DoesNotExist:
        pass

"""
Assign i to the index of the answer for the highest level on the course.
Go backwards through the levels.
If a student feels confident on a level in the second half of the course
check they are also confident on the previous 2 levels, start them on that level.
If not decrement i and repeat the process.
If the level is in the first half of the course, start a student on the level
above the highest one they are confident completing.
Otherwise start the student on level 1
"""
def get_starting_level(answers):
    #assign i the value of the index of the highest level in the course
    i = len(answers)-1
    #the level is in second part of the course
    while i >= len(answers)//2:
        if answers[i] == "True":
            #check for confidence on the previous 2 levels too
            if answers[i-1] == "True" and answers[i-2]== "True":
                return i+1
        i -= 1
    while i > 0:
        if answers[i] == "True":
            return i+1
        else:
            i -= 1
    return 1



"""
Get a list of the questions the student has previously answered incorrectly.
Shuffle the list.
If the list has less that 5 questions display them all
Else display the first 5 questions in the list
"""
def get_revision_resources(user_id):
    student = StudentProfile.objects.get(user_id = user_id)
    #get incorrect answers from db
    incorrect_questions = IncorrectAnswer.objects.filter(user = student.user_id)
    #convert queryset into a list so it can be shuffled
    incorrect_questions = list(incorrect_questions)
    number_of_q = len(incorrect_questions)
    shuffle(incorrect_questions)
    if len(incorrect_questions) > 5:
        incorrect_questions = incorrect_questions[0:5]

    return (incorrect_questions, number_of_q)

"""
Go through the answers to the signup quiz and add them to list
"""
def get_user_answers(request):
    answers = []
    for key, value in request.POST.items():
        if key != 'csrfmiddlewaretoken':
            answers.append(value)
    return answers

"""
Update student level and signup_quiz_completed after they
complete the signup quiz
"""
def update_student(level, user):
    student = StudentProfile.objects.get(user_id = user.id)
    student.signup_quiz_completed = True
    student.level = level
    student.starting_level = level
    student.save()

