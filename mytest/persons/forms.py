from django import forms
from mytest.persons.models import Person


class PersonForm(forms.ModelForm):
    birth_date = forms.CharField(label='Date of birth')

    class Meta:
        model = Person
