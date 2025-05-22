from mango_disease_app.models import Disease, Orchard, Record, UserProfile
from django.shortcuts import render
from django.db.models import Prefetch
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

def plan(request):
    page_data = generate_plan(request.user)
    return render(request, 'mango_disease_app/plan.html', {'page_data':page_data})
