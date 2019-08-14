from django.db import models
from django.contrib.auth.models import User
from custom_users.models import StudentProfile

"""
Students have a Level. Exams and Lessons have a level.
This can be used to match appropriate exam or lesson to
student.
"""
#Exams have a level and a title.
class Exam(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    level = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.level) +" "+self.title

# Questions belong to an exam.
class Question(models.Model):
    exam = models.ManyToManyField(Exam)
    text = models.CharField(max_length=1000, unique = True)
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

    def __str__(self):
        return self.text

# Model for storing a StudentProfile users answers
class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=1000)
    user = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user', 'question', 'user_answer']]

    def __str__(self):
        return self.user_answer

# Model to store information about which exams a user has completed
class CompletedExam(models.Model):
    user = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    level = models.IntegerField(default = 1)
    percentage = models.IntegerField(default = 1)

    class Meta:
        unique_together = ['user', 'exam', 'level']

    def __str__(self):
        return self.user.user.username+" "+self.exam.title
