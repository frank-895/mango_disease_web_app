from django import forms
from .models import *

class addDiseaseRecord(forms.ModelForm):
    class Meta:
        model = Record
        exclude = []