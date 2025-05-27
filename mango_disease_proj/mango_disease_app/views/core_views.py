from mango_disease_app.models import Disease, Orchard, Record, UserProfile, Case
from django.shortcuts import render
from django.db.models import Prefetch, Max
from mango_disease_app.services.planner import generate_plan

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

def account(request):
    plan_items = generate_plan(request.user) #Use Franks generate_plan
    plan_by_orchard = {item['orchard']: item for item in plan_items} #Organise each orharcd into an array
    #Get Records
    record_qs = (
        Record.objects 
            .select_related("case")
            .order_by("-recordedAt", "-id") #Order by Newest first
    )
    #Query for active cases and their records
    active_cases_qs = (
        Case.objects
            .filter(status__iexact="active") #Get active cases regardless of capitalisation
            .select_related('disease')  #join on disease
            .prefetch_related(          #look for records
                Prefetch("record_set",  
                        queryset=record_qs,
                        to_attr="records") #save as cases.records
            )
    )
    #Main Orchard Query
    orchards = (Orchard.objects
                    .filter(user=request.user) #Restrict Orchard Access
                    .select_related('variety', 'location') #Join with variet and location
                    .prefetch_related(      #Look for cases next
                        Prefetch("case_set",
                                 queryset=active_cases_qs,
                                 to_attr="active_cases") #save as orchards.active_cases
                    )
                )
    for o in orchards:
        o.plan = plan_by_orchard.get(o.orchardName)
    
                            
    return render(request, 'mango_disease_app/account.html',{'orchards' : orchards})

def admin_tools(request):
    return render(request, 'mango_disease_app/admin_forms/admintools.html')

def plan(request):
    page_data = generate_plan(request.user)
    return render(request, 'mango_disease_app/plan.html', {'page_data':page_data})
