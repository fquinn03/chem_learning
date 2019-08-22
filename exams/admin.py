from django.contrib import admin
from .models import (Answer, CompletedExam, Exam,
Formula_Question, MCQ_Question, UserAnswer,
Written_Question, IncorrectAnswer)

class AnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Answer, AnswerAdmin)

class ExamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Exam, ExamAdmin)

class Written_QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Written_Question, Written_QuestionAdmin)

class MCQ_QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(MCQ_Question, MCQ_QuestionAdmin)

class Formula_QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Formula_Question, Formula_QuestionAdmin)

class UserAnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAnswer, UserAnswerAdmin)

class IncorrectAnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(IncorrectAnswer, IncorrectAnswerAdmin)

class CompletedExamAdmin(admin.ModelAdmin):
    pass

admin.site.register(CompletedExam, CompletedExamAdmin)
