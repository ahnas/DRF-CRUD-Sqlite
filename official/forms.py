from dataclasses import field
from django import forms

from employeeapi.models import Employee
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name','id':'name','name':'name'}),
            'type': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Type','id':'type','name':'type'}),
            'age': NumberInput(attrs={'class': 'required form-control', 'placeholder': 'Your Age','id':'age','name':'age'}),
            'description': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Description','id':'description','name':'description'}),
        }