from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.db.models import Prefetch
from .forms import *
from .models import *
from .services.planner import generate_plan

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
    form = addDiseaseRecord(request.POST or None, user=request.user)
    
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
    orchards = (Orchard.objects
                    .filter(user=request.user)
                    .select_related('variety', 'location')
                    .prefetch_related(
                        Prefetch(
                            'record_set',
                            queryset=(
                                Record.objects
                                    .select_related('disease')
                                    .order_by("-recordedAt", '-id')[:5] #Last 5 Records  https://forum.djangoproject.com/t/prefetch-top-n-most-recent-related-objects/39767
                            ),
                            to_attr='recent_records'
                        )
                    )
                    
                )
                            
    return render(request, 'mango_disease_app/account.html',{'orchards' : orchards})

def admin_tools(request):
    return render(request, 'mango_disease_app/admintools.html')

def add_disease(request):
    post_data = None
    form = DiseaseForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        new_disease = form.save()  
        post_data = {
            'name':new_disease.diseaseName,
            'type':new_disease.type,
        }
        form = DiseaseForm()
    
    return render(request, 'mango_disease_app/add_disease.html', {'form': form, 'new_disease': post_data})

def add_location(request):
    post_data = None
    form = LocationForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        new_location = form.save()  
        post_data = {
            'name':new_location.locationName,
        }
        form = LocationForm()
    
    return render(request, 'mango_disease_app/add_location.html', {'form': form, 'new_location': post_data})

def add_variety(request):
    post_data = None
    form = VarietyForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        new_variety = form.save()  
        post_data = {
            'name':new_variety.varietyName,
        }
        form = VarietyForm()
    
    return render(request, 'mango_disease_app/add_variety.html', {'form': form, 'new_variety': post_data})

def plan(request):
    page_data = generate_plan(request.user)
    return render(request, 'mango_disease_app/plan.html', {'page_data':page_data})

def build(request):
    new_orchard = None
    form = OrchardForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        orchard = form.save(commit=False)
        orchard.user = request.user
        orchard.save()
        new_orchard = orchard
        form = OrchardForm()  # Reset the form after submission

    # Get the orchards for the current user
    orchards = Orchard.objects.filter(user=request.user)

    return render(request, 'mango_disease_app/build.html', {
        'form': form,
        'new_orchard': new_orchard,
        'orchards': orchards,
    })
def edit_orchard(request, orchard_id):
    orchard = Orchard.objects.get(id=orchard_id, user=request.user)
    form = OrchardForm(request.POST or None, instance=orchard)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('build')

    return render(request, 'mango_disease_app/edit_orchard.html', {
        'form': form,
        'orchard': orchard,
    })

from django.shortcuts import get_object_or_404

def delete_orchard(request, orchard_id):
    orchard = get_object_or_404(Orchard, id=orchard_id, user=request.user)

    if request.method == 'POST':
        orchard.delete()
        return redirect('build')

    return render(request, 'mango_disease_app/confirm_delete.html', {'orchard': orchard})


def add_orchard(request): 

    new_orchard = None 

 

    if request.method == 'POST': 

        form = OrchardForm(request.POST) 

        if form.is_valid(): 

            orchard = form.save(commit=False) 

            orchard.user = request.user  # Attach the logged-in user 

            orchard.save() 

            new_orchard = orchard 

            form = OrchardForm()  # Clear the form after submission 

    else: 

        form = OrchardForm() 

 

    return render(request, 'mango_disease_app/build.html', { 

        'form': form, 

        'new_orchard': new_orchard 

    }) 


def orchard_list(request):
    search_query = request.GET.get('search', '')
    orchards = Orchard.objects.all()

    if search_query:
        orchards = orchards.filter(orchardName__icontains=search_query)

    return render(request, 'mango_disease_app/build.html', {'orchards': orchards, 'search_query': search_query})