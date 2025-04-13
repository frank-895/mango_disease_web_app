from django.shortcuts import render
from .author_card import AuthorCard
from .data_model import data_model
import os
    
######### Define Authors #########
frank = AuthorCard("Frank Snelling",
                   "S367853",
                   "Computer Science",
                   "Travel, Food & Wine",
                   50,
                   30,
                   10,
                   90,
                   "Frank.png")

michael = AuthorCard("Michael Lewis",
                   "S342724",
                   "Secondary Education",
                   "Ludology, Squash, Hiking",
                   50,
                   80,
                   60,
                   70)


fakepest = data_model("NAME (PEST)",True,4,8,"SDESC-P","LDESC-P","CONTROL-P")
fakepest2 = data_model("NAME 2 (PEST)",True,4,8,"SDESC-P 2","LDESC-P 2","CONTROL-P 2")
fakedisease = data_model("NAME (DISEASE)",False,2,7,"SDESC-D","LDESC-D","CONTROL-D")
fakedisease2 = data_model("NAME 2 (DISEASE)",False,2,7,"SDESC-D 2","LDESC-D 2","CONTROL-D 2")

authors = [frank, michael]

def home(request):
    return render(request, 'mango_disease_app/index.html')

def diseases(request):
    diseases = [fakepest,fakedisease,fakepest2,fakedisease2]
    page_data = {'diseases': diseases}
    return render(request, 'mango_disease_app/diseases.html', page_data)

def about(request):       
    page_data = {'cards': authors}
    return render(request, 'mango_disease_app/about.html', page_data)