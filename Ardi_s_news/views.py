
from django.http import HttpResponse
from django.shortcuts import render

sections = ['Aktualitet', 'Politike', 'Ekonomi', 'Opinion', 'Sporti', 'Kulture'] 

def home(request):
    return render(request, 'Faqja_kryesore/home.html', {'sections': sections, })
    

