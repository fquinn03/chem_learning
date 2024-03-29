from django.db import models
from django.contrib.auth.models import User
from custom_users.models import StudentProfile

"""
These are the models form exams and questions.
Students have a Level.
Exams and Lessons also have a level.
Levels can be used to match appropriate exam or lesson to student.
"""
#Exams have a level and a title.
class Exam(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    level = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.level) +" "+self.title

# Questions belong to an exam.
class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.CharField(max_length=250, unique = True)
    questionimage = models.CharField(max_length=250, null=True, blank = True)
    questiongif = models.CharField(max_length=250, null=True, blank = True)
    questionscript = models.CharField(max_length=250, null=True, blank = True)
    review = models.CharField(max_length=1000)
    reviewimage = models.CharField(max_length=250, null=True, blank = True)
    reviewgif = models.CharField(max_length=250, null=True, blank = True)
    reviewscript = models.CharField(max_length=250, null=True, blank = True)

    def __str__(self):
        return self.text

# Inherits from Question. Written_Answer Style Question
class Written_Question(Question):
    is_written = models.BooleanField(default = True)

    class Meta:
        verbose_name="Written_Question"

# Inherits from Question. Mutliple Choice Style Question
class MCQ_Question(Question):
    is_MCQ = models.BooleanField(default = True)

    class Meta:
        verbose_name="MCQ_Question"

# Inherits from Question. The answer contains a chemical formula
class Formula_Question(Question):
    is_formula = models.BooleanField(default = True)

    class Meta:
        verbose_name="Formula_Question"

# Model for the correct answers or mutiple choice answer options
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    correct = models.BooleanField(default = False)
    correct_spelling = models.BooleanField(default = True)
    correct_answer_to_display = models.BooleanField(default = False)

    def __str__(self):
        return self.text

# Model for storing a student's answers to the quiz
class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=1000)
    user = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_answer

# Model to store information about which exams a student has completed
class CompletedExam(models.Model):
    user = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    level = models.IntegerField(default = 1)
    percentage = models.IntegerField(default = 1)
    attempt = models.IntegerField(default = 1)

    def __str__(self):
        return self.user.user.username+" "+self.exam.title

# Model for storing a stuedent's incorrect answers
class IncorrectAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.username+ " "+self.question.text
