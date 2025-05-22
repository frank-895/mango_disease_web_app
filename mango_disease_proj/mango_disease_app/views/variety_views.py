from django.shortcuts import render, redirect, get_object_or_404

from mango_disease_app.forms import VarietyForm
from mango_disease_app.models import Variety

def add_variety(request):
    post_data = None
    form = VarietyForm(request.POST or None)
    varieties = Variety.objects.all()
    
    if request.method == 'POST' and form.is_valid():
        new_variety = form.save()  
        post_data = {
            'name':new_variety.varietyName,
        }
        form = VarietyForm()
    
    return render(request, 'mango_disease_app/admin_forms/add_variety.html', {
        'form': form,
        'new_variety': post_data,
        'varieties':varieties,
    })

def edit_variety(request, variety_id):
    variety = get_object_or_404(Variety, id=variety_id)
    form = VarietyForm(request.POST or None, instance=variety)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('add_variety')

    return render(request, 'mango_disease_app/admin_forms/edit_form_base.html', {
        'form': form,
        'entity_name': variety,
    })

def delete_variety(request, variety_id):
    variety = get_object_or_404(Variety, id=variety_id)
    variety.delete()
    return redirect('add_variety')