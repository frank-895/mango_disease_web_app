from django.shortcuts import render, redirect, get_object_or_404

from mango_disease_app.forms import DiseaseForm
from mango_disease_app.models import Disease


def add_disease(request):
    post_data = None
    form = DiseaseForm(request.POST or None)
    diseases = Disease.objects.all()
    
    if request.method == 'POST' and form.is_valid():
        new_disease = form.save()  
        post_data = {
            'name':new_disease.diseaseName,
            'type':new_disease.type,
        }
        form = DiseaseForm()
    
    return render(request, 'mango_disease_app/admin_forms/add_disease.html', {
        'form': form, 
        'new_disease': post_data,
        'diseases':diseases,
    })

def edit_disease(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)
    form = DiseaseForm(request.POST or None, instance=disease)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('add_disease')

    return render(request, 'mango_disease_app/admin_forms/edit_form_base.html', {
        'form': form,
        'entity_name': disease,
    })

def delete_disease(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)
    disease.delete()
    return redirect('add_disease')