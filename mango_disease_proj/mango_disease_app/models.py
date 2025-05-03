from django.db import models
from django.core import validators
from django.utils import timezone

class Variety(models.Model):
    varietyID = models.AutoField(primary_key=True)
    varietyName = models.CharField()
    
    def __str__(self):
        return self.varietyName

class Location(models.Model):
    locationID = models.AutoField(primary_key=True)
    locationName = models.CharField()
    
    def __str__(self):
        return self.locationName

class Orchard(models.Model):
    orchardID = models.AutoField(primary_key=True)
    orchardName = models.CharField()
    noTreesRow = models.IntegerField()
    noTreesColumn = models.IntegerField()
    varietyID = models.ForeignKey(
        Variety,
        on_delete=models.PROTECT
    )
    locationID = models.ForeignKey(
        Location,
        on_delete=models.PROTECT
    )
    
    def __str__(self):
        return self.orchardName

class Disease(models.Model):
    diseaseID = models.AutoField(primary_key=True)
    diseaseName = models.CharField()
    severity = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    spreadability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    shortDescription = models.CharField()
    longDescription = models.CharField()
    controlMethod = models.CharField()
    
    def __str__(self):
        return self.diseaseName

plantParts = {
    'leaf':'Leaf',
    'stem':'Stem',
    'fruit':'Fruit',
}

class Record(models.Model):
    recordID = models.AutoField(primary_key=True)
    orchardID = models.ForeignKey(
        Orchard,
        on_delete=models.PROTECT
    )
    recordedAt = models.DateTimeField(default=timezone.now)
    partOfPlant = models.CharField(choices=plantParts)
    disease = models.ForeignKey(Disease, related_name='records', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.orchardID} - Disease: {self.disease}"
    
class LocationDisease(models.Model):
    locationID = models.ForeignKey(
        Location,
        on_delete=models.PROTECT
    )
    diseaseID = models.ForeignKey(
        Disease,
        on_delete=models.PROTECT
    )
    locationSusecptability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])

class VarietyDiseaseSusceptible(models.Model):
    varietyID = models.ForeignKey(
        Variety,
        on_delete=models.PROTECT
    )
    diseaseID = models.ForeignKey(
        Disease,
        on_delete=models.PROTECT
    )
    varietySusecptability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
