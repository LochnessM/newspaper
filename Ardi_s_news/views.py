
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'Faqja_kryesore/home.html')
    

