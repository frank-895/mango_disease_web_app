#https://dev.to/sarahhudaib/context-processors-in-django-15h2

from .models import Disease 

def disease_menu(request):
    return {'navs': Disease.objects.all()}