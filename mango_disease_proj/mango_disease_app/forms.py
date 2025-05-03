from django import forms
from .models import *
from datetime import date

class addDiseaseRecord(forms.ModelForm):
    class Meta:
        model = Record
        #exclude = ['orchardID']
        fields = ['orchardID', 'recordedAt', 'partOfPlant', 'disease']
        labels = {
            'orchardID':"Choose your orchard",
            'recordedAt': "Enter date of recording",
            'partOfPlant': "Choose which part of plant was impacted",
            'disease': "Choose the disease affecting the plant",
        }
        widgets = {
            'recordedAt': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'max': date.today().isoformat()
            }),
        }