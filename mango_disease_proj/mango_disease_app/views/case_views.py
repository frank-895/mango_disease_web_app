from django.shortcuts import render

from mango_disease_app.forms import CaseForm
from mango_disease_app.models import Case

def cases(request):
    cases = Case.objects.filter(orchard__user=request.user)
    
    return render(request, 'mango_disease_app/cases.html', {
        'cases': cases,
    })
def new_case(request):
    post_data = None
    form = CaseForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        new_case = form.save()  
        post_data = {
            'disease': new_case.disease.diseaseName,
            'orchard': new_case.orchard.orchardName
        }
        form = CaseForm()
    
    return render(request, 'mango_disease_app/new_case.html', {'form': form, 'new_case': post_data})