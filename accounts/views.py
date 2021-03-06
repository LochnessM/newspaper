from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Ardi_s_news.decorators import unauthenticated_user

# Create your views here.

@unauthenticated_user
def login_request(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')    
        else:
            messages.info(request, 'Emri i perdoruesit ose fjalekalimi nuk jane te sakte!') 
            return redirect('login_url')          

@login_required(login_url = 'login_url')
def logout_request(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')  

@login_required(login_url = 'login_url')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')   

    
