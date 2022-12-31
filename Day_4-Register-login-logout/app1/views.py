from django.shortcuts import render
from django.http import HttpResponse
from . forms import CustomUserCreationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register(request):
    """Register user"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('user created')
        else:
            return HttpResponse('error occured')
        
    form = CustomUserCreationForm()
    return render(request, 'app1\lregister.html', {'form':form})

def user_login(request):
    """Login user using built-in AuthenticatCionForm."""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('login successful')
            else:
                return HttpResponse('error occured while login.')
    
    form = AuthenticationForm()
    return render(request, "app1/login.html", {"form":form})

def user_logout(request):
    """logout user from system."""
    logout(request)
    return HttpResponse('user logout')
