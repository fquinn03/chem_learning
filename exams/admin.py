from django.contrib import admin
from .models import Answer, Exam, Formula_Question, Level, MCQ_Question, UserAnswer, Written_Question



class AnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Answer, AnswerAdmin)

class ExamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Exam, ExamAdmin)

class LevelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Level, LevelAdmin)

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
