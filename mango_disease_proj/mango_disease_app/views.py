from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import *
from .models import *

def userlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'mango_disease_app/userlogin.html', {'form':form})

def register(request):
    #Register form posts to itself on submit
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #Info Validation
        if form.is_valid():
            #Save to User DD and Login
            login(request, form.save())
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, 'mango_disease_app/register.html', {'form':form})

def home(request):
    return render(request, 'mango_disease_app/index.html')

def diseases(request):
    categories = {
        'diseases': Disease.objects.filter(type='disease'),
        'pests': Disease.objects.filter(type='pest'),
    }
    return render(request, 'mango_disease_app/diseases.html', {'data':categories})

def ind_disease(request, name):
    try:
        disease = Disease.objects.get(diseaseName=name)
    except Disease.DoesNotExist:
        return render(request, 'mango_disease_app/ind_disease.html')
    return render(request, 'mango_disease_app/ind_disease.html',{'disease':disease})

def about(request):    
    authors = UserProfile.objects.all() 
    page_data = {'cards': authors}
    return render(request, 'mango_disease_app/about.html', page_data)

def add_record(request):
    post_data = None
    form = addDiseaseRecord(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        new_record = form.save()  
        post_data = {
            'orchard':new_record.orchardID,
            'time':new_record.recordedAt,
            'partOfPlant':new_record.partOfPlant,
            'disease':new_record.disease,
        }
        form = addDiseaseRecord()
    
    return render(request, 'mango_disease_app/record.html', {'form': form, 'new_record': post_data})

def account(request):
    return render(request, 'mango_disease_app/account.html')

def plan(request):
    return render(request, 'mango_disease_app/plan.html')

def build(request):
    return render(request, 'mango_disease_app/build.html')