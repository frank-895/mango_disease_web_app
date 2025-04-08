from django.shortcuts import render
from .models import AuthorCard

def home(request):
    return render(request, 'mango_disease_app/index.html')

def diseases(request):
    return render(request, 'mango_disease_app/diseases.html')

def about(request):
    cards = AuthorCard.objects.all()
    
    # Scale the personality traits to a 100 scale (for percentage)
    for card in cards:
        card.collaborator_independent = int(card.collaborator_independent) * 10
        card.bigPicture_detailOriented = int(card.bigPicture_detailOriented) * 10
        card.communicator_listener = int(card.communicator_listener) * 10
        card.creative_practical = int(card.creative_practical) * 10
    
    page_data = {'cards': cards}
    return render(request, 'mango_disease_app/about.html', page_data)
