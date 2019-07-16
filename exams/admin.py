from django.contrib import admin
from .models import Answer, Exam, Level, Question, UserAnswer

class AnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Answer, AnswerAdmin)

class ExamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Exam, ExamAdmin)

class LevelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Level, LevelAdmin)

class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)

class UserAnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAnswer, UserAnswerAdmin)
