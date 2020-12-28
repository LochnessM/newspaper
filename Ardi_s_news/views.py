
from django.http import HttpResponse
from django.shortcuts import render
from artikulli.models import artikulli

sections = ['Aktualitet', 'Politike', 'Ekonomi', 'Opinion', 'Sporti', 'Kulture'] 

def home(request):
    artikujt = artikulli.objects.all()
    return render(request, 'Faqja_kryesore/home.html', {'sections': sections, 'artikujt': artikujt})
    

