from django.contrib import admin
import mango_disease_app.models as models
#from mango_disease_app.models import User, Variety, Location, Orchard, Disease, Record, LocationDisease, VarietyDiseaseSusceptible, OrchardUser, RecordDisease

# Model Registration
admin.site.register(models.User)
admin.site.register(models.Variety)
admin.site.register(models.Location)
admin.site.register(models.Orchard)
admin.site.register(models.Disease)
admin.site.register(models.Record)
admin.site.register(models.LocationDisease)
admin.site.register(models.VarietyDiseaseSusceptible)
admin.site.register(models.OrchardUser)
admin.site.register(models.RecordDisease)