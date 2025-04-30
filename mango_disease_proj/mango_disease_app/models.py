from django.db import models
from django.core import validators
from django.utils import timezone

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField()

class Variety(models.Model):
    varietyID = models.AutoField(primary_key=True)

class Location(models.Model):
    locationID = models.AutoField(primary_key=True)
    locationName = models.CharField()

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

class Disease(models.Model):
    diseaseID = models.AutoField(primary_key=True)
    diseaseName = models.CharField()
    severity = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    spreadability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])
    shortDescription = models.CharField()
    longDescription = models.CharField()
    controlMethod = models.CharField()

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


class LocationDisease(models.Model):
    locationID = models.ForeignKey(
        Location,
        on_delete=models.PROTECT
    )
    diseaseID = models.ForeignKey(
        Disease,
        on_delete=models.PROTECT
    )
    susecptability = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)])

class VarietyDiseaseSusceptible(models.Model):
    varietyID = models.ForeignKey(
        Variety,
        on_delete=models.PROTECT
    )
    diseaseID = models.ForeignKey(
        Disease,
        on_delete=models.PROTECT
    )

class OrchardUser(models.Model):
    orchardID = models.ForeignKey(
        Orchard,
        on_delete=models.PROTECT
    )
    userID = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

class RecordDisease(models.Model):
    recordID = models.ForeignKey(
        Record,
        on_delete=models.PROTECT
    )
    diseaseID = models.ForeignKey(
        Disease,
        on_delete=models.PROTECT
    )
