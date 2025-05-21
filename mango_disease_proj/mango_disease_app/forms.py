from django import forms
from .models import *
from datetime import date


# class addDiseaseRecord(forms.ModelForm):
#     def __init__(self, *args, **kwargs): #https://stackoverflow.com/questions/74964200/limit-choices-inside-an-input-django/74965183
#         user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
        
#         if user is not None:
#             self.fields['orchardID'].queryset = Orchard.objects.filter(user=user)
#     class Meta:
#         model = Record
#         #exclude = ['orchardID']
#         fields = ['orchardID', 'recordedAt', 'partOfPlant', 'disease', 'numberOfTreesChecked', 'numberOfTreesInfected']
#         labels = {
#             'orchardID':"Choose your orchard",
#             'recordedAt': "Enter date of recording",
#             'partOfPlant': "Choose which part of plant was impacted",
#             'disease': "Choose the disease affecting the plant",
#             'numberOfTreesChecked': "Enter the number of trees you checked",
#             'numberOfTreesInfected': "Enter how many trees you checked were infected",
#         }
#         widgets = {
#             'recordedAt': forms.DateInput(attrs={
#                 'type': 'date',
#                 'class': 'form-control',
#                 'max': date.today().isoformat()
#             }),
#         }

            
#     def clean(self): # see documentation https://docs.djangoproject.com/en/5.1/ref/forms/validation/
#         cleaned_data = super().clean()
#         orchard = cleaned_data.get('orchardID')
#         no_checked = cleaned_data.get('numberOfTreesChecked')
#         no_infected = cleaned_data.get('numberOfTreesInfected')
#         total_trees = orchard.noTreesRow * orchard.noTreesColumn
        
#         if  orchard and no_checked and no_infected:
#             total_trees = orchard.noTreesRow * orchard.noTreesColumn
#             if no_checked > total_trees:
#                 self.add_error('numberofTreesChecked', f"Must be between 1 and total trees in orchard ({total_trees}).")
#             if no_infected > no_checked:
#                 self.add_error('numberofTreesInfected', f"Must be between 1 and number of trees checked ({no_checked}).")




class OrchardForm(forms.ModelForm):
    class Meta:
        model = Orchard
        fields = ['orchardName', 'noTreesRow', 'noTreesColumn', 'area', 'variety', 'location']
        labels = {
            'orchardName': "Orchard Name",
            'noTreesRow': "Number of Rows of Trees",
            'noTreesColumn': "Number of Columns of Trees",
            'area': "Area (in square meters)",
            'variety': "Mango Variety",
            'location': "Location",
        }
        widgets = {
            'orchardName': forms.TextInput(attrs={'class': 'form-control'}),
            'noTreesRow': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'noTreesColumn': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'area': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'variety': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_area(self):
        area = self.cleaned_data.get('area')
        if area < 0:
            raise ValidationError("Area must be a positive value.")
        return area
    


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['diseaseName','type','severity','spreadability','shortDescription','longDescription','controlMethod','image']
        labels = {
            'diseaseName': "Name of the disease / pest",
            'type': "Whether it is a disease or a pest",
            'severity': "How severe the disease / pest is",
            'spreadability': "How easily the disease / pest spreads between trees",
            'shortDescription': "Short snippet to describe the disease / pest",
            'longDescription': "Full description of the disease / pest",
            'controlMethod': "How the disease / pest can be controlled or managed",
            'image': "Example image of the disease / pest",
        }
        
        
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['locationName','hemisphere']
        labels = {
            'locationName': "Name of the location",
            'hemisphere': "Which hemisphere the location is in",
        }
        
        
        
class VarietyForm(forms.ModelForm):
    class Meta:
        model = Variety
        fields = ['varietyName']
        labels = {
            'varietyName': "Name of the tree variety",
        }
        
class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['disease','orchard','partOfPlant']
        labels = {
            'disease': 'The disease or pest found',
            'orchard': 'The orchard it was found in',
            'partOfPlant': 'The part of the plant affected',
        }
        
class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['case','orchard','recordedAt','numberOfTreesChecked','numberOfTreesInfected']
        labels = {
            'recordedAt': "Time of recording",
            'numberOfTreesChecked': "Number of trees checked",
            'numberOfTreesInfected': "Number of trees infected",
        }