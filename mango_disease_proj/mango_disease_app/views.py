from django.shortcuts import render

def home(request):
    return render(request, 'mango_disease_app/home.html')

def diseases(request):
    return render(request, 'mango_disease_app/diseases.html')

def about(request):
    return render(request, 'mango_disease_app/about.html')
