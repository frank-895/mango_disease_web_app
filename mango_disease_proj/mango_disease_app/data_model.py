
import os
from django.conf import settings # to get path to static files

class data_model:
    def __init__ (self,
        # Disease / Pest Details
        name:str, pest:bool, severity:int, spreadability:int,
        
        # Disease / Pest Information
        sdesc:str, ldesc:str, control:str,
        
        # Image file path (will default if left empty)
        image:str=None
    ):
        # assigning and validating attributes
        self.name = name
        self.pest = pest
        self.severity = severity
        self.spreadability = spreadability
        
        self.sdesc = sdesc
        self.ldesc = ldesc
        self.control = control
        
        self.image = image