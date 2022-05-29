from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import createUserForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm

from django.contrib import messages
from.forms import createUserForm
from.models import Profile
# Create your views here.

def signup(request):
    
    # signup form
    form = createUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,  'account created for ' + user)
            return redirect('login')
    else:
        form = createUserForm()
    return render(request, 'signup.html', {'form': form})

    # login form
    
    def loginPage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post')
            else:
                messages.info(request, 'username OR password is incorrect')
                
                return redirect("login")
        return render(request, 'login.html')
    
    
    # logout views
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post')
            else:
                messages.info(request, 'username OR password is incorrect')
                return redirect("login")

    
    return render(request,'signup.html')



def logout(request):
    return render(request, 'logout.html' )

