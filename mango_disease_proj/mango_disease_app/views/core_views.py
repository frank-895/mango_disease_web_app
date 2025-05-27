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
    #Query for 5 most recent records
    record_qs = (
        Record.objects
            .select_related("case")
            .order_by("-recordedAt", "-id")
    )
    #Query for active cases
    active_cases_qs = (
        Case.objects
            .filter(status__iexact="active")
            .select_related('disease')
            .prefetch_related(
                Prefetch("record_set",
                        queryset=record_qs,
                        to_attr="records")
            )
    )
    #Main Orchard Query
    orchards = (Orchard.objects
                    .filter(user=request.user)
                    .select_related('variety', 'location')
                    .prefetch_related(
                        Prefetch("case_set",
                                 queryset=active_cases_qs,
                                 to_attr="active_cases")
                    )
                )
                            
    return render(request, 'mango_disease_app/account.html',{'orchards' : orchards})

def admin_tools(request):
    return render(request, 'mango_disease_app/admin_forms/admintools.html')

def plan(request):
    page_data = generate_plan(request.user)
    return render(request, 'mango_disease_app/plan.html', {'page_data':page_data})
