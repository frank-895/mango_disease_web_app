from django.shortcuts import render
from .models import AuthorCard

def home(request):
    return render(request, 'mango_disease_app/index.html')

def diseases(request):
    return render(request, 'mango_disease_app/diseases.html')

def about(request):
    cards = AuthorCard.objects.all()
    page_data = {'cards': cards}
    return render(request, 'mango_disease_app/about.html', page_data)
