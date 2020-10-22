from django import forms
from durationwidget import *


class MyForm(forms.Form):
    name = forms.CharField(label="User name", disabled=True)
    email = forms.EmailField(error_messages={'required': 'Please enter E-mail'})
    password = forms.CharField(max_length=20, min_length=5,
                               widget=forms.PasswordInput())
    profile_picture = forms.ImageField(widget=forms.FileInput)
    additional_file = forms.FileField(widget=forms.FileInput)
    age = forms.IntegerField(required=False, help_text="Enter you age")
    agreement = forms.BooleanField(required=False)
    average_score = forms.FloatField(required=False, initial=10.1)
    birthday = forms.DateField(required=False, widget=forms.SelectDateWidget)
    # work_experience = forms.DurationField(widget=TimeDurationWidget())
    gender = forms.ChoiceField(choices=[("1", "man"), ("2", "female")])

