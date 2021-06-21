from django import forms
from .models import *


class ClassForm(forms.ModelForm):

    class Meta:
        model= ClassStreams
        fields= ["class_title", 'students_number', 'teacher']

class StudentsForm(forms.ModelForm):

    class Meta:
        model= Student
        fields=['admission', 'name', 'student_class']