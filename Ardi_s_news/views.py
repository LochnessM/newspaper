
from django.http import HttpResponse
from django.shortcuts import render
from artikulli.models import artikulli
from django.core.paginator import Paginator
import json


artikujt_a = artikulli.objects.all().order_by('-data')
paginator_aktualitet = Paginator(artikujt_a, 1)
aktualitet_num_pages = paginator_aktualitet.num_pages

artikujt_p = artikulli.objects.filter(kategoria = 'Politike').order_by('-data')
paginator_politike = Paginator(artikujt_p, 1)
politike_num_pages = paginator_politike.num_pages

artikujt_e = artikulli.objects.filter(kategoria = 'Ekonomi').order_by('-data')
paginator_ekonomi = Paginator(artikujt_e, 1)
ekonomi_num_pages = paginator_ekonomi.num_pages

artikujt_o = artikulli.objects.filter(kategoria = 'Opinion').order_by('-data')
paginator_opinion = Paginator(artikujt_o, 1)
opinion_num_pages = paginator_opinion.num_pages

artikujt_s = artikulli.objects.filter(kategoria = 'Sporti').order_by('-data')
paginator_sporti = Paginator(artikujt_s, 1)
sporti_num_pages = paginator_sporti.num_pages

artikujt_k = artikulli.objects.filter(kategoria = 'Kulture').order_by('-data')
paginator_kulture = Paginator(artikujt_k, 1)
kulture_num_pages = paginator_kulture.num_pages


pages = {'aktualitet_num_pages' : aktualitet_num_pages, 
        'politike_num_pages' : politike_num_pages, 
        'ekonomi_num_pages' : ekonomi_num_pages, 
        'opinion_num_pages' : opinion_num_pages, 
        'sporti_num_pages' : sporti_num_pages, 
        'kulture_num_pages' : kulture_num_pages
        }


def home(request): 
    if request.GET :
        if request.GET.__contains__('aktualitet_page'):
            artikuj = paginator_aktualitet.page(request.GET.get('aktualitet_page'))
            artikuj_as_json = json.dumps([ artikull.as_json() for artikull in artikuj ])
            return HttpResponse(artikuj_as_json)
        if request.GET.__contains__('politike_page'):
            artikuj = paginator_politike.page(request.GET.get('politike_page'))
            artikuj_as_json = json.dumps([ artikull.as_json() for artikull in artikuj ])
            return artikuj_as_json
        if request.GET.__contains__('ekonomi_page'):
            artikuj = paginator_ekonomi.page(request.GET.get('ekonomi_page'))
            artikuj_as_json = json.dumps([ artikull.as_json() for artikull in artikuj ])
            return artikuj_as_json
        if request.GET.__contains__('opinion_page'):
            artikuj = paginator_opinion.page(request.GET.get('opinion_page'))
            artikuj_as_json = json.dumps([ artikull.as_json() for artikull in artikuj ])
            return artikuj_as_json
        if request.GET.__contains__('sporti_page'):
            artikuj = paginator_sporti.page(request.GET.get('sporti_page'))
            artikuj_as_json = json.dumps([ artikull.as_json() for artikull in artikuj ])
            return artikuj_as_json
        if request.GET.__contains__('kulture_page'):
            artikuj = paginator_kulture.page(request.GET.get('kulture_page'))
            artikuj_as_json = json.dumps([ artikull.as_json() for artikull in artikuj ])
            return artikuj_as_json                    
    else :       
        aktualitet = paginator_aktualitet.page(1)
        politike = paginator_politike.page(1)
        ekonomi = paginator_ekonomi.page(1)
        opinion = paginator_opinion.page(1)
        sporti = paginator_sporti.page(1)
        kulture = paginator_kulture.page(1)

        sections = {'aktualitet': aktualitet, 
                    'politike': politike, 
                    'ekonomi': ekonomi, 
                    'opinion': opinion, 
                    'sporti': sporti, 
                    'kulture': kulture}

        return render(request, 'Faqja_kryesore/home.html', {'sections': sections, 'pages': pages})
    
