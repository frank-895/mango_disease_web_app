from django.contrib import admin
import mango_disease_app.models as models

# Model Registration
admin.site.register(models.UserProfile)
admin.site.register(models.Variety)
admin.site.register(models.Location)
admin.site.register(models.Orchard)
admin.site.register(models.Disease)
admin.site.register(models.Record)
admin.site.register(models.LocationDisease)
admin.site.register(models.VarietyDisease)