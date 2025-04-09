from django.shortcuts import render
from .models import DiseaseItem
import os

######## AUTHOR CARD CLASS #########
# Snelling, April 9 2025

class AuthorCard:
    def __init__(self,
                 name:str, 
                 student_number:str,
                 degree:str, 
                 interests:str,
                 image:str, # place image in static/images and pass file name here. 
                 collaborator_independent:int,
                 bigPicture_detailOriented:int, 
                 communicator_listener:int,
                 creative_practical:int):
        
        # validate and assign class attributes
        self.name = self.validate_string(name, "name", 30)
        self.student_number = self.validate_string(student_number, "student_number", 7)
        self.degree = self.validate_string(degree, "degree", 30)
        self.interests = self.validate_string(interests, "interests", 100)
        self.image = (image)
        self.collaborator_independent = self.validate_int(collaborator_independent, "collaborator_independent", 0, 100)
        self.bigPicture_detailOriented = self.validate_int(bigPicture_detailOriented, "bigPicture_detailOriented", 0, 100)
        self.communicator_listener = self.validate_int(communicator_listener, "communicator_listener", 0, 100)
        self.creative_practical = self.validate_int(creative_practical, "creative_practical", 0, 100)
    
    def validate_string(self, string, var_name, max_len):
        """Function checks that string is type string and has length of less than max_len."""
        if not isinstance(string, str) or len(string) == 0:
            raise ValueError("%s must be non-empty string." % var_name)
        if len(string) > max_len:
            raise ValueError("%s must be less than %d characters" % (var_name, max_len))
        
        return string
    
    def validate_int(self, integer, var_name, min_val, max_val):
        """Function checks that integer is type int and has value of between min_val and max_val."""
        if not isinstance(integer, int):
            raise ValueError("%s must be non-empty." % var_name)
        if integer < min_val  or integer > max_val:
            raise ValueError("%s must be between %d and %d" % (var_name, min_val, max_val))
        
        return integer
    
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

authors = [frank]

def home(request):
    return render(request, 'mango_disease_app/index.html')

def diseases(request):
    diseases = DiseaseItem.objects.all()
    page_data = {'diseases': diseases}
    return render(request, 'mango_disease_app/diseases.html', page_data)

def about(request):       
    page_data = {'cards': authors}
    return render(request, 'mango_disease_app/about.html', page_data)