from django.shortcuts import render

from mango_disease_app.forms import RecordForm
from mango_disease_app.models import Record, Case

def records(request, case_id):
    case = Case.objects.get(id=case_id)
    cRecords = Record.objects.filter(case=case)
    
    return render(request, 'mango_disease_app/record.html', {
        'records': cRecords,
        'caseID': case_id,
    })
    
def add_record(request, case_id):
    post_data = None
    rCase = Case.objects.get(id=case_id)
    form = RecordForm(request.POST or None, initial={'case':rCase,'orchard':rCase.orchard})

    if request.method == 'POST' and form.is_valid():
        new_record = form.save()
        post_data = {
            'time':new_record.recordedAt,
        }
        form = RecordForm()

    return render(request, 'mango_disease_app/add_record.html', {
        'form': form, 
        'new_record': post_data,
        'caseID': case_id,
        })