from django import forms
import datetime


by = [1984, 1983, 1982]
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class StudentForm(forms.Form):
    name = forms.CharField(max_length=10, label='please enter your name')
    roll = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    email = forms.EmailField(required=False, initial='@gmail.com')
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    choose_birth_date = forms.DateField(widget=forms.SelectDateWidget(years=by))
    today = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)