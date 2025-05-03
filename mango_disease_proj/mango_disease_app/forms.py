from django import forms
from .models import *

class addDiseaseRecord(forms.ModelForm):
    class Meta:
        model = Record
        exclude = []
        labels = {
            'orchardId':"TEMPORARY - needs to be changed to whoever is logged in",
            'recordedAt': "Enter time of recording: ",
            'partOfPlant': "Choose which part of plant was impacted: ",
        }