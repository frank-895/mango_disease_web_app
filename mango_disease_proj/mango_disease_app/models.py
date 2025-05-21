from django.db import models
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

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
    varietySusceptability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    
    def __str__(self):
        return self.varietyName

class Location(models.Model):
    HEMISPHERES = [
        ('north', 'Northern'),
        ('south', 'Southern'),
    ]
    locationName = models.CharField(max_length=255)
    hemisphere = models.CharField(choices=HEMISPHERES, max_length=5, default='south')
    locationSusceptability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    
    def __str__(self):
        return self.locationName

class Orchard(models.Model):
    orchardName = models.CharField(max_length=255)
    noTreesRow = models.IntegerField()
    noTreesColumn = models.IntegerField()
    area = models.IntegerField(validators=[validators.MinValueValidator(0)])
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
    DISEASE_TYPES = [
        ('pest', 'Pest'),
        ('disease', 'Disease')
    ]
    
    diseaseName = models.CharField(max_length=255)
    type = models.CharField(choices=DISEASE_TYPES, max_length=7, default=DISEASE_TYPES[1][1])
    severity = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    spreadability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    shortDescription = models.TextField()
    longDescription = models.TextField()
    controlMethod = models.TextField()
    image = models.ImageField(upload_to="disease_images/", default="disease_images/default.JPG")
    
    def __str__(self):
        return self.diseaseName

class Case(models.Model):
    STATUS = [
        ('active', 'Active'),
        ('resolved', 'Resolved'),
    ]
    PLANT_PARTS = [
        ('leaf', 'Leaf'),
        ('stem', 'Stem'),
        ('fruit', 'Fruit'),
    ]
    
    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE,
        null=True
    )
    orchard = models.ForeignKey(
        Orchard,
        on_delete=models.CASCADE,
        null=True
    )
    status = models.CharField(choices=STATUS, max_length=8, default=STATUS[0][1], null=True)
    partOfPlant = models.CharField(choices=PLANT_PARTS, max_length=5, null=True)

    def __str__(self):
        return f"Case for {self.orchard} - Disease: {self.disease} on the {self.partOfPlant}"
    
class Record(models.Model):
    # clean method handles validation for case and orchard foreign keys
    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    
    orchard = models.ForeignKey(
        Orchard,
        on_delete=models.CASCADE,
        null=True, # clean method handles validation
        blank=True,
    )
    
    recordedAt = models.DateField(default=timezone.now)
    numberOfTreesChecked = models.IntegerField(validators=[validators.MinValueValidator(1)])
    numberOfTreesInfected = models.IntegerField(validators=[validators.MinValueValidator(1)])
    
    def __str__(self):
        return f"Record for {self.case} - Recorded at: {self.recordedAt}"

    def clean(self): # https://docs.djangoproject.com/en/5.1/ref/forms/validation/
        if not self.case and not self.orchard:
            raise ValidationError('Record must be linked to a Case or an Orchard.')
        if self.case and not self.orchard: # automatically link case to Orchard too
            self.orchard = self.case.orchard