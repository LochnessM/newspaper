
from django.http import HttpResponse
from django.shortcuts import render
from artikulli.models import artikulli
from django.core.paginator import Paginator

artikujt_a = artikulli.objects.all().order_by('-data')
paginator_aktualitet = Paginator(artikujt_a, 1)

artikujt_p = artikulli.objects.filter(kategoria = 'Politike').order_by('-data')
paginator_politike = Paginator(artikujt_p, 1)

artikujt_e = artikulli.objects.filter(kategoria = 'Ekonomi').order_by('-data')
paginator_ekonomi = Paginator(artikujt_e, 1)

artikujt_o = artikulli.objects.filter(kategoria = 'Opinion').order_by('-data')
paginator_opinion = Paginator(artikujt_o, 1)

artikujt_s = artikulli.objects.filter(kategoria = 'Sporti').order_by('-data')
paginator_sporti = Paginator(artikujt_s, 1)

artikujt_k = artikulli.objects.filter(kategoria = 'Kulture').order_by('-data')
paginator_kulture = Paginator(artikujt_k, 1)


def home(request):    
    aktualitet = load_aktualitet(request)
    politike = load_politike(request)
    ekonomi = load_ekonomi(request)
    opinion = load_opinion(request)
    sporti = load_sporti(request)
    kulture = load_kulture(request)

    sections = {'Aktualitet': aktualitet, 
                'Politike': politike, 
                'Ekonomi': ekonomi, 
                'Opinion': opinion, 
                'Sporti': sporti, 
                'Kulture': kulture}

    return render(request, 'Faqja_kryesore/home.html', {'sections': sections})
    


def load_aktualitet(request):
    page_num = request.GET.get('Aktualitet_page', 1)
    return paginator_aktualitet.page(page_num)

def load_politike(request):
    page_num = request.GET.get('Politike_page', 1)
    return paginator_politike.page(page_num)

def load_ekonomi(request):
    page_num = request.GET.get('Ekonomi_page', 1)
    return paginator_ekonomi.page(page_num)

def load_opinion(request):
    page_num = request.GET.get('Opinion_page', 1)
    return paginator_opinion.page(page_num)

def load_sporti(request):
    page_num = request.GET.get('Sporti_page', 1)
    return paginator_sporti.page(page_num)

def load_kulture(request):
    page_num = request.GET.get('Kulture_page', 1)
    return paginator_kulture.page(page_num)