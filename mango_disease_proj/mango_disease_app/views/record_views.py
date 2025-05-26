from django.shortcuts import render, redirect

from mango_disease_app.forms import RecordForm
from mango_disease_app.models import Record, Case

def records(request, case_id):
    case = Case.objects.get(id=case_id)
    cRecords = Record.objects.filter(case=case)
    
    return render(request, 'mango_disease_app/record.html', {
        'records': cRecords,
        'id': case_id,
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
    
def delete_record(request, record_id):
    record = Record.objects.get(id=record_id,orchard__user=request.user)
    
    if request.method == 'POST':
        record.delete()
        return redirect("cases")
    
    return render(request, 'mango_disease_app/delete_record.html', {'record':record})

def edit_record(request, record_id):
    post_data = None
    record = Record.objects.get(id=record_id, orchard__user=request.user)
    form = RecordForm(request.POST or None, instance=record)

    if request.method == 'POST' and form.is_valid():
        new_record = form.save()  
        post_data = {
            'recordedAt': new_record.recordedAt,
            'case': new_record.case,
            'id': new_record.id,
        }
        form = RecordForm()

    return render(request, 'mango_disease_app/edit_record.html', {
        'form': form,
        'new_record': post_data,
        'id': record.id
    })