from django import forms
from .models import *
from datetime import date

class addDiseaseRecord(forms.ModelForm):
    class Meta:
        model = Record
        #exclude = ['orchardID']
        fields = ['orchardID', 'recordedAt', 'partOfPlant', 'disease', 'numberOfTreesChecked', 'numberOfTreesInfected']
        labels = {
            'orchardID':"Choose your orchard",
            'recordedAt': "Enter date of recording",
            'partOfPlant': "Choose which part of plant was impacted",
            'disease': "Choose the disease affecting the plant",
            'numberOfTreesChecked': "Enter the number of trees you checked",
            'numberOfTreesInfected': "Enter how many trees you checked were infected",
        }
        widgets = {
            'recordedAt': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'max': date.today().isoformat()
            }),
        }
        
    def clean(self): # see documentation https://docs.djangoproject.com/en/5.1/ref/forms/validation/
        cleaned_data = super().clean()
        orchard = cleaned_data.get('orchardID')
        no_checked = cleaned_data.get('numberOfTreesChecked')
        no_infected = cleaned_data.get('numberOfTreesInfected')
        total_trees = orchard.noTreesRow * orchard.noTreesColumn
        
        if  orchard and no_checked and no_infected:
            total_trees = orchard.noTreesRow * orchard.noTreesColumn
            if no_checked > total_trees:
                self.add_error('numberofTreesChecked', f"Must be between 1 and total trees in orchard ({total_trees}).")
            if no_infected > no_checked:
                self.add_error('numberofTreesInfected', f"Must be between 1 and number of trees checked ({no_checked}).")