from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from mango_disease_app.forms import LocationForm
from mango_disease_app.models import Location

def add_location(request):
    post_data = None
    form = LocationForm(request.POST or None)
    locations = Location.objects.all()
    
    if request.method == 'POST' and form.is_valid():
        new_location = form.save()  
        messages.success(request, f"{new_location.locationName} was successfully added.")
        form = LocationForm()
    
    return render(request, 'mango_disease_app/admin_forms/add_location.html', {
        'form': form, 
        'locations':locations,
    })

def edit_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    form = LocationForm(request.POST or None, instance=location)

    if request.method == 'POST' and form.is_valid():
        new_location = form.save()
        messages.success(request, f"{new_location.locationName} was successfully edited.")
        return redirect('add_location')

    return render(request, 'mango_disease_app/admin_forms/edit_form_base.html', {
        'form': form,
        'entity_name': location,
    })

def delete_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    location.delete()
    messages.success(request, f"{location.locationName} was successfully deleted.")    
    return redirect('add_location')