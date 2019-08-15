from .models import StudentProfile, TeacherProfile
from exams.models import CompletedExam

def sign_up_quiz_already_completed(user):
    student = StudentProfile.objects.get(user_id = user.id)
    return not student.signup_quiz_completed

def have_teacher_details(user):
    teacher = TeacherProfile.objects.get(user_id = user.id)
    return teacher.details_added

def have_student_details(user):
    student = StudentProfile.objects.get(user_id = user.id)
    return student.details_added

def have_student_signup(user):
    student = StudentProfile.objects.get(user_id = user.id)
    return student.signup_quiz_completed

def user_is_student(user):
    try:
        StudentProfile.objects.get(user_id = user.id)
        return True
    except:
        return False

def user_is_teacher(user):
    try:
        TeacherProfile.objects.get(user_id = user.id)
        return True
    except:
        return False

def exam_not_done_before(user):
    student = StudentProfile.objects.get(user_id = user.id)
    return CompletedExam.objects.filter(user = user.id).filter(exam = student.next_exam_id ).filter(attempt = student.attempt)

def is_finished(user):
    student = StudentProfile.objects.get(user_id = user.id)
    return student.level > 4
