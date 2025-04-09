from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

######## DISEASE CLASS #########
# Patrick, March 2025

class DiseaseItem(models.Model):
    
    # Disease / Pest Details
    name = models.CharField(
        max_length=30,
        default="No Name Entered",
        help_text="Enter disease or pest name.",
    )
    
    pest = models.BooleanField(
        default=False,
        help_text="Set to TRUE if this is a pest, FALSE if this is a disease.",
    )
    
    severity = models.SmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(10)],
        default=1,
        help_text="Severity of disease / pest on a scale from from 1 to 10, with 10 being most severe.",
    )
    
    spreadability = models.SmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(10)],
        default=1,
        help_text="How quickly the disease / pest spreads on a scale from from 1 to 10, with 10 being the fastest.",
    )
    
    image = models.ImageField(
        upload_to="disease_images/",
        default="author_images/default_disease.jpg",
        help_text="Upload an image or a default disease (Anthracnose) will be provided."
        
    )
    
    # Disease / Pest Information
    sdesc = models.TextField(
        default="No description given",
        help_text="Enter a short description of the disease or pest to be displayed on a list.",
    )
    
    ldesc = models.TextField(
        default="No description given",
        help_text="Enter a long description of the disease or pest to be displayed on an individual page.",
    )
    
    control = models.TextField(
        default="No control method given",
        help_text="Method(s) of controlling or eliminating the disease / pest.",
    )



######## AUTHOR CLASS #########
# Snelling, April 7 2025


# add help text
class AuthorCard(models.Model):
    
    # AUTHOR DETAILS
    name = models.CharField(
        max_length=30,
        default="No Name Entered",
        help_text="Enter contributor name.",
    )
    
    student_number = models.CharField(
        max_length=7,
        default="S000000",
        help_text="Enter CDU Student Number from ID card.",
    )
    
    degree = models.CharField(
        max_length=30, 
        default="Computer Science",
        help_text="Enter degree at CDU.",
    )
    
    interests = models.CharField(
        max_length=100,
        default="No interests",
        help_text="Enter a few interests in less than 100 characters.",
    )
    
    image = models.ImageField(
        upload_to="author_images/",
        default="author_images/default.png",
        help_text="Upload an image or a default empty profile will be provided."
    )

    # PERSONALITY TRAITS
    # scored on 0 to 10 scale: 0 is leftmost, 10 is rightmost.

    # Collaborator - Independent
    collaborator_independent = models.SmallIntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(10)],
            default=5,
            help_text="0 is for a strong collaborator, 10 is for most independent.",
        )
    
    # Big picture - Detail oriented
    bigPicture_detailOriented = models.SmallIntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(10)],
            default=5,
            help_text="0 is for focus on big picture, 10 is for focus on details.",
        )
    
    # Communicator - Listener
    communicator_listener = models.SmallIntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(10)],
            default=5,
            help_text="0 is for a strong communicator, 10 is for a strong listener.",
        )
    
    # Creative - Practical
    creative_practical = models.SmallIntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(10)],
            default=5,
            help_text="0 is for most creative, 10 is for most practical.",
        )