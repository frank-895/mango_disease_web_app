from django.shortcuts import render
from .models import DiseaseItem
from .author_card import AuthorCard
import os
    
# Define Authors
frank = AuthorCard("Frank Snelling",
                   "S367853",
                   "Computer Science",
                   "Python, Travel, Food & Wine",
                   "Frank.png",
                   50,
                   30,
                   10,
                   90)

michael = AuthorCard("Michael Lewis",
                   "S342724",
                   "Secondary Education",
                   "Ludology, Squash, Hiking",
                   "blank.png",
                   50,
                   80,
                   60,
                   70)


authors = [frank, michael]

def home(request):
    return render(request, 'mango_disease_app/index.html')

def diseases(request):
    diseases = DiseaseItem.objects.all()
    page_data = {'diseases': diseases}
    return render(request, 'mango_disease_app/diseases.html', page_data)

def about(request):       
    page_data = {'cards': authors}
    return render(request, 'mango_disease_app/about.html', page_data)