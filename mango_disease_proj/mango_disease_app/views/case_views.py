from django.shortcuts import render, redirect

from mango_disease_app.forms import CaseForm
from mango_disease_app.models import Case

def cases(request):  
    cases = Case.objects.filter(orchard__user=request.user)
      
    categories = {
        'Active': cases.filter(status__iexact='active'),
        'Resolved': cases.filter(status__iexact='resolved'),
    }
    
    return render(request, 'mango_disease_app/account/cases.html', {
        'cases': cases,
        'data': categories,
    })

def new_case(request):
    post_data = None
    form = CaseForm(request.POST or None, user=request.user)
    
    if request.method == 'POST' and form.is_valid():
        new_case = form.save()  
        post_data = {
            'disease': new_case.disease.diseaseName,
            'orchard': new_case.orchard.orchardName,
            'id': new_case.id,
        }
        form = CaseForm(user=request.user)
    
    return render(request, 'mango_disease_app/account/forms/new_case.html', {'form': form, 'new_case': post_data})

def manage_case(request, case_id):
    case = Case.objects.get(id=case_id,orchard__user=request.user)
    
    if request.method == 'POST':
        i=request.POST.__getitem__('action')
        if i=='resolve':
            case.status = 'resolved'
            case.save()
            return redirect('cases')
        elif i=='delete':
            case.delete()
            return redirect('cases')
    
    return render(request, 'mango_disease_app/account/forms/manage_case.html', {'case':case})

def edit_case(request, case_id):
    post_data = None
    case = Case.objects.get(id=case_id, orchard__user=request.user)
    form = CaseForm(request.POST or None, instance=case, user=request.user)

    if request.method == 'POST' and form.is_valid():
        new_case = form.save()  
        post_data = {
            'disease': new_case.disease.diseaseName,
            'orchard': new_case.orchard.orchardName,
            'id': new_case.id,
        }
        form = CaseForm(user=request.user)

    return render(request, 'mango_disease_app/account/forms/edit_case.html', {
        'form': form,
        'new_case': post_data,
        'id': case.id
    })