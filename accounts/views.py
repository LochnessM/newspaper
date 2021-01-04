from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from artikulli.models import artikulli

# Create your views here.

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


def logout_request(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')  


def dashboard(request):
    return render(request, 'accounts/dashboard.html')   


def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        kategoria = request.POST.get('kategoria')
        image = request.FILES.get('image')
        new_article = artikulli(author = request.user, title = title, description = description, kategoria = kategoria, image = image)
        new_article.save()
    return redirect('dashboard')    
