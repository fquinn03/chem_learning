"""
from django import forms
from .models import UserAnswer
from users.models import StudentProfile
from exams.models import Question, Answer

class UserAnswerForm(forms.Form):
    class Meta:
        model= UserAnswer
        fields= ["question", "user_answer", "user"]

class ReadOnlyText(forms.TextInput):
  input_type = 'text'

  def render(self, name, value, attrs=None):
     if value is None:
         value = ''
     return value

class QuestionForm(forms.Form):

    questions = Question.objects.all()

    for question in questions:
        answers = question.answer_set.all
        question = forms.CharField(widget=ReadOnlyText, label=question.text)
        answers = forms.MultipleChoiceField(
                required=True,
                widget=forms.CheckboxSelectMultiple,
                choices=answers,
            )
"""
