from django import forms

class ExampleForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    roll_number = forms.IntegerField(
        help_text="Enter 11 digit roll number"
    )