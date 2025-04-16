#https://dev.to/sarahhudaib/context-processors-in-django-15h2

from .views import disease_list 

def disease_menu(request):
    return {'navs': disease_list}