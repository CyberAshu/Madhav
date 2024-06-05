from django import forms

class EnrollForm(forms.Form):
    roll_number = forms.CharField(label='Roll Number', max_length=20)
