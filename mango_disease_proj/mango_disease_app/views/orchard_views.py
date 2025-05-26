from django.shortcuts import render, redirect, get_object_or_404


from mango_disease_app.forms import OrchardForm
from mango_disease_app.models import Orchard

def add_orchard(request):
    new_orchard = None
    form = OrchardForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        orchard = form.save(commit=False)
        orchard.user = request.user
        orchard.save()
        new_orchard = orchard
        form = OrchardForm()  # Reset the form after submission

    # Get the orchards for the current user
    orchards = Orchard.objects.filter(user=request.user)

    return render(request, 'mango_disease_app/add_orchard.html', {
        'form': form,
        'new_orchard': new_orchard,
        'orchards': orchards,
    })
    
def edit_orchard(request, orchard_id):
    orchard = Orchard.objects.get(id=orchard_id, user=request.user)
    form = OrchardForm(request.POST or None, instance=orchard)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('build')

    return render(request, 'mango_disease_app/edit_orchard.html', {
        'form': form,
        'orchard': orchard,
    })

def delete_orchard(request, orchard_id):
    orchard = get_object_or_404(Orchard, id=orchard_id, user=request.user)

    if request.method == 'POST':
        orchard.delete()
        return redirect('add_orchard')

    return render(request, 'mango_disease_app/confirm_delete.html', {'orchard': orchard})

def orchard_list(request):
    search_query = request.GET.get('search', '')

    # Filter only orchards created by the logged-in user
    orchards = Orchard.objects.filter(user=request.user)

    # Apply search if a query is given
    if search_query:
        orchards = orchards.filter(orchardName__icontains=search_query)

    return render(request, 'mango_disease_app/add_orchard.html', {
        'orchards': orchards,
        'search_query': search_query
    })