from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def userlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'mango_disease_app/userlogin.html', {'form':form})

def register(request):
    #Register form posts to itself on submit
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #Info Validation
        if form.is_valid():
            #Save to User DD and Login
            login(request, form.save())
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, 'mango_disease_app/register.html', {'form':form})