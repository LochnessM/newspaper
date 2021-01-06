from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from .models import artikulli


@login_required(login_url = 'login_url')
def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        kategoria = request.POST.get('kategoria')
        image = request.FILES.get('image')
        new_article = artikulli(author = request.user, title = title, description = description, kategoria = kategoria, image = image)
        new_article.save()
    return redirect('dashboard')


def delete_article():
    pass

def update_article():
    pass