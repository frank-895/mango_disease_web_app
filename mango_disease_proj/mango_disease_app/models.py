from django.db import models
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_superuser': True},
    )
    student_number = models.CharField(max_length=7)
    degree = models.CharField(max_length=30)
    interests = models.CharField(max_length=100)
    image = models.ImageField(upload_to="author_images/", default="author_images/blank.png")

    collaborator_independent = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=5)
    bigPicture_detailOriented = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=5)
    communicator_listener = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=5)
    creative_practical = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=5)

    def __str__(self):
        return f"{self.user.username}'s AuthorCard"

class Variety(models.Model):
    varietyName = models.CharField(max_length=255)
    
    def __str__(self):
        return self.varietyName

class Location(models.Model):
    locationName = models.CharField(max_length=255)
    
    def __str__(self):
        return self.locationName

class Orchard(models.Model):
    orchardName = models.CharField(max_length=255)
    noTreesRow = models.IntegerField()
    noTreesColumn = models.IntegerField()
    variety = models.ForeignKey(
        Variety,
        on_delete=models.PROTECT
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # If a user is deleted, delete the orchard too
    )
    
    def __str__(self):
        return self.orchardName

class Disease(models.Model):
    diseaseName = models.CharField(max_length=255)
    severity = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    spreadability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    shortDescription = models.TextField()
    longDescription = models.TextField()
    controlMethod = models.TextField()
    image = models.ImageField(upload_to="disease_images/", default="disease_images/default.JPG")
    
    def __str__(self):
        return self.diseaseName

class Record(models.Model):
    PLANT_PARTS = [
        ('leaf', 'Leaf'),
        ('stem', 'Stem'),
        ('fruit', 'Fruit'),
    ]
    
    orchardID = models.ForeignKey(
        Orchard,
        on_delete=models.CASCADE
    )
    recordedAt = models.DateField(default=timezone.now)
    partOfPlant = models.CharField(choices=PLANT_PARTS, max_length=5)
    disease = models.ForeignKey(Disease, related_name='records', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Record for {self.orchardID} - Disease: {self.disease} at {self.recordedAt}"
    
class LocationDisease(models.Model):
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )
    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
    )
    locationSusceptability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    
    def __str__(self):
        return f"{self.location} susceptibility to {self.disease}"

class VarietyDisease(models.Model):
    variety = models.ForeignKey(
        Variety,
        on_delete=models.CASCADE
    )
    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
    )
    varietySusceptability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    
    def __str__(self):
        return f"{self.variety} susceptibility to {self.disease}"