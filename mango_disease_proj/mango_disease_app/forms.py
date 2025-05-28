from django import forms
from .models import *
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        fields = ['locationName','hemisphere', 'locationSusceptability']
        labels = {
            'locationName': "Name of the location",
            'hemisphere': "Which hemisphere the location is in",
            'locationSusceptability': "How suscpetible is this location to disease?"
        }
        
class VarietyForm(forms.ModelForm):
    class Meta:
        model = Variety
        fields = ['varietyName', 'varietySusceptability']
        labels = {
            'varietyName': "Name of the tree variety",
            'varietySusceptability': "How susceptible is this variety to disease?"
        }
        
class CaseForm(forms.ModelForm):    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['orchard'].queryset = Orchard.objects.filter(
                user=user
            )
    
    class Meta:
        ## NOTE FOR PATRICK :) - orchard needs to be limited to the user's orchards only. 
        model = Case
        fields = ['disease','orchard','partOfPlant']
        labels = {
            'disease': 'The disease or pest found',
            'orchard': 'The orchard it was found in',
            'partOfPlant': 'The part of the plant affected',
        }
        
class RecordForm(forms.ModelForm):    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['case'].queryset = Case.objects.filter(
                orchard__user=user,
                status__iexact='active',
            )
            
    class Meta:
        model = Record
        fields = ['case','recordedAt','numberOfTreesChecked','numberOfTreesInfected']
        labels = {
            'recordedAt': "Date of recording",
            'numberOfTreesChecked': "Number of trees checked",
            'numberOfTreesInfected': "Number of trees infected",
        }
        widgets = {
            'recordedAt': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'max': date.today().isoformat()
            }),
        }
        
    ### NOTE FOR PATRICK - THIS MIGHT BE HELPFUL, I WROTE IT FOR THE OLD RECORD FUNCTION TO VALIDATE IF THE NUMBER CHECKED AND NUMBER INFECTED IS LESS THAN THE NUMBER OF TREES IN THE ORCHARD
    # def clean(self): # see documentation https://docs.djangoproject.com/en/5.1/ref/forms/validation/
    #     cleaned_data = super().clean()
    #     orchard = cleaned_data.get('orchardID')
    #     no_checked = cleaned_data.get('numberOfTreesChecked')
    #     no_infected = cleaned_data.get('numberOfTreesInfected')
    #     total_trees = orchard.noTreesRow * orchard.noTreesColumn

    #     if  orchard and no_checked and no_infected:
    #         total_trees = orchard.noTreesRow * orchard.noTreesColumn
    #         if no_checked > total_trees:
    #             self.add_error('numberofTreesChecked', f"Must be between 1 and total trees in orchard ({total_trees}).")
    #         if no_infected > no_checked:
    #             self.add_error('numberofTreesInfected', f"Must be between 1 and number of trees checked ({no_checked}).")
    
class AddUserProfileForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(is_superuser=False).exclude(userprofile__isnull=False),
        label="Select an existing user to promote to superuser"
    )
    
    class Meta:
        model = UserProfile
        fields = ['student_number','degree','interests','image', 'collaborator_independent','bigPicture_detailOriented','communicator_listener','creative_practical']
        labels = {
            'student_number': "Enter the student number of the author",
            'degree': "Enter the degree of the author",
            'interests': "List a few interests",
            'collaborator_independent': "Rate the author between 1 and 10, where 1 is strong collaborator and 10 is more independent",
            'bigPicture_detailOriented': "Rate the author between 1 and 10, where 1 is big picture and 10 is detail oriented",
            'communicator_listener': "Rate the author between 1 and 10, where 1 is a great communicator and 10 is a great listener",
            'creative_practical': "Rate the author between 1 and 10, where 1 is most creative and 10 is most practical",
            'image': "Image of the author (optional)",
        }

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        labels = {
            'student_number': "Enter the student number of the author",
            'degree': "Enter the degree of the author",
            'interests': "List a few interests",
            'collaborator_independent': "Rate the author between 1 and 10, where 1 is strong collaborator and 10 is more independent",
            'bigPicture_detailOriented': "Rate the author between 1 and 10, where 1 is big picture and 10 is detail oriented",
            'communicator_listener': "Rate the author between 1 and 10, where 1 is a great communicator and 10 is a great listener",
            'creative_practical': "Rate the author between 1 and 10, where 1 is most creative and 10 is most practical",
            'image': "Image of the author (optional)",
        }

       
       
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        