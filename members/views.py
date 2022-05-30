
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import createUserForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib import messages
from.forms import createUserForm
from.models import Profile

# signup form
def signup(request):
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
                return redirect('signup')
        else:
            messages.info(request, 'username OR password is incorrect')
            return redirect("login")
        return render(request, 'loginPage.html')
    
# logout

def logoutPage(request):
        logout(request)
        return redirect('login')

