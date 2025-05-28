from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages

from mango_disease_app.forms import AddUserProfileForm, EditUserProfileForm
from mango_disease_app.models import UserProfile
from mango_disease_app.forms import CustomUserCreationForm


def userlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'mango_disease_app/auth/userlogin.html', {'form':form})

def register(request):
    #Register form posts to itself on submit
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        #Info Validation
        if form.is_valid():
            #Save to User DD and Login
            login(request, form.save())
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, 'mango_disease_app/auth/register.html', {'form':form})

def add_admin(request):
    post_data = None
    form = AddUserProfileForm(request.POST or None, request.FILES or None)
    admins = UserProfile.objects.filter(user__is_superuser=True)

    if request.method == 'POST' and form.is_valid():
        profile = form.save(commit=False)

        # Get selected user from form and assign to profile
        user = form.cleaned_data['user']
        profile.user = user

        # Promote user to superuser
        user.is_superuser = True
        user.save()

        profile.save()

        messages.success(request, f"{user.get_full_name() or user.username} was successfully promoted to admin.")
        form = AddUserProfileForm()  # reset form

    return render(request, 'mango_disease_app/admin_forms/add_admin.html', {
        'form': form,
        'admins': admins,
    })


def edit_admin(request, admin_id):
    profile = get_object_or_404(UserProfile, id=admin_id)
    form = EditUserProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f"{profile.user.get_full_name() or profile.user.username}'s admin profile was updated.")
        return redirect('add_admin')

    return render(request, 'mango_disease_app/admin_forms/edit_form_base.html', {
        'form': form,
        'entity_name': profile.user.get_full_name() or profile.user.username,
    })

def delete_admin(request, admin_id):
    profile = get_object_or_404(UserProfile, id=admin_id)
    user = profile.user
    profile.delete()
    user.is_superuser = False
    user.save()
    messages.success(request, f"{user.get_full_name() or user.username} was removed as an admin.")
    return redirect('add_admin')