from django import forms
from .models import *

class addDiseaseRecord(forms.ModelForm):
    diseases = forms.ModelMultipleChoiceField(
        queryset=Disease.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Diseases Found"
    )

    class Meta:
        model = Record
        exclude = []