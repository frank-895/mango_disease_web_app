from django.db import models

######## DISEASE CLASS #########
# Patrick, March 2025

# class data_item():
    
#     def __init__(self,name,pest=False,snip='Brief Description / Snippet',ldesc='Long Description',image='Image URL',severity='Severe',control='Control method'):
        
#         self.name=name          # Name of the disease / pest
        
#         if pest:                # Whether the item is a pest or a disease
#             self.pd = 'Pest'
#         else:
#             self.pd = 'Disease'
        
#         self.snip=snip          # Snippet of information to be displayed on the list page
        
#         self.ldesc=ldesc        # Longer description to be displayed on the disease / pest's specific page
        
#         self.image=image        # Related image
        
#         self.severity=severity  # Severity of threat
        
#         self.control=control    # Method of controlling / removing the disease / pest
        
# # Creation of 7 data items
# item1 = data_item('Item One')
# item2 = data_item('Item Two')
# item3 = data_item('Item Three')
# item4 = data_item('Item Four')
# item5 = data_item('Item Five')
# item6 = data_item('Item Six')
# item7 = data_item('Item Seven')

# # List of all items
# item_list = [item1,item2,item3,item4,item5,item6,item7]

######## AUTHOR CLASS #########
# Snelling, April 7 2025

from django.core.validators import MinValueValidator, MaxValueValidator

# add help text
class AuthorCard(models.Model):
    name = models.CharField(max_length=30)
    degree = models.CharField(max_length=30, default="Computer Science")
    interests = models.CharField(max_length=100, default="No interests")
    image = models.ImageField(upload_to='author_images/', default='author_images/default.png')

    # PERSONALITY TRAITS
    # scored on 0 to 10 scale: 0 is leftmost, 10 is rightmost.

    # Collaborator - Independent
    CI = models.SmallIntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(10)],
            default=5,
        )
    
    # Big picture - Detail oriented
    BD = models.SmallIntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(10)],
            default=5,
        )
    
    # Communicator - Listener
    CI = models.SmallIntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(10)],
            default=5,
        )
    
    # Creative - Practical
    CI = models.SmallIntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(10)],
            default=5,
        )