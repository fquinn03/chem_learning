from django import forms
from custom_users.models import Class_id

class AddClassForm(forms.ModelForm):
    class Meta:
        model = Class_id
        fields = ("name",)
