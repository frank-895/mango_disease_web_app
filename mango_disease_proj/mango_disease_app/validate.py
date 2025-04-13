### Validation methods ###
# Snelling, April 12 2025

import os
from django.conf import settings # to get path to static files

def validate_string(string:str, var_name:str, max_len:int):
    """Function checks that string is type string and has length of less than max_len."""
    if not isinstance(string, str) or len(string) == 0:
        raise ValueError("%s must be non-empty string." % var_name)
    if len(string) > max_len:
        raise ValueError("%s must be less than %d characters" % (var_name, max_len))
    
    return string

def validate_int(integer:int, var_name:str, min_val:int, max_val:int):
    """Function checks that integer is type int and has value of between min_val and max_val."""
    if not isinstance(integer, int):
        raise ValueError("%s must be an integer." % var_name)
    if integer < min_val  or integer > max_val:
        raise ValueError("%s must be between %d and %d" % (var_name, min_val, max_val))
    
    return integer

def validate_img(filename:str):
    """Function checks that image exists in the static/images directory."""
    if filename is None or filename is "":
        return None
    
    path = os.path.join(settings.BASE_DIR, 'mango_disease_app', "static", "images", filename)
    print(f"Checking if the image exists at: {path}")
    
    if not os.path.isfile(path):
        raise FileNotFoundError("%s not found in static/images/" % filename)
    
    return filename