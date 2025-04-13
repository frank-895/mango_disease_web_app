######## AUTHOR CARD CLASS #########
# Snelling, April 12 2025

from .validate import validate_img, validate_int, validate_string

class AuthorCard:
    def __init__(self,
                 name:str, 
                 student_number:str,
                 degree:str, 
                 interests:str,
                 
                 # score on a scale of 0 to 100, where 0 is leftmost attribute and 100 is rightmost attribute
                 collaborator_independent:int,
                 bigPicture_detailOriented:int, 
                 communicator_listener:int,
                 creative_practical:int,
                 
                 # place image in static/images and pass file name here or optionally leave empty
                 image:str=None): 
        
        # validate and assign class attributes
        self.name = validate_string(name, "name", 30)
        self.student_number = validate_string(student_number, "student_number", 7)
        self.degree = validate_string(degree, "degree", 30)
        self.interests = validate_string(interests, "interests", 100)
        self.collaborator_independent = validate_int(collaborator_independent, "collaborator_independent", 0, 100)
        self.bigPicture_detailOriented = validate_int(bigPicture_detailOriented, "bigPicture_detailOriented", 0, 100)
        self.communicator_listener = validate_int(communicator_listener, "communicator_listener", 0, 100)
        self.creative_practical = validate_int(creative_practical, "creative_practical", 0, 100)
        self.image = validate_img(image)