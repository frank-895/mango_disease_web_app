### Data model class ###
# Dunn, April 13 2025

from .validate import validate_img, validate_int, validate_string

class data_model:
    def __init__ (self,
        # Disease / Pest Details
        name:str, pest:bool, severity:int, spreadability:int,
        
        # Disease / Pest Information
        sdesc:str, ldesc:str, control:str,
        
        # Image file path (will default if left empty)
        image:str=None
    ):
        #Color meter UI
        def meterclass(value):
            if value >= 7:
                return 'meter-high'
            elif value >= 4:
                return 'meter-med'
            else:
                return 'meter-low'
        # assigning and validating attributes
        self.name = validate_string(name, "name", 30)
        self.pest = pest
        self.severity = validate_int(severity, "severity", 1, 10)
        self.severityclass = meterclass(self.severity)
        self.spreadability = validate_int(spreadability, "spreadability", 1, 10)
        self.spreadabilityclass = meterclass(self.spreadability)
        self.sdesc = validate_string(sdesc, "sdesc", 200)
        self.ldesc = validate_string(ldesc, "ldesc", 1000)
        self.control = validate_string(control, "control", 1000)
        
        self.image = validate_img(image)