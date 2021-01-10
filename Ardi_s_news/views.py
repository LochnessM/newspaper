
from django.http import HttpResponse
from django.shortcuts import render
from artikulli.models import artikulli
from django.core.paginator import Paginator


def home(request):
    artikujt_aktualitet = artikulli.objects.all().order_by('-data')
    paginator_aktualitet = Paginator(artikujt_aktualitet, 8)
    aktualitet_page_num = request.GET.get('aktualitet_page', 1)
    artikujt_aktualitet = paginator_aktualitet.page(aktualitet_page_num)

    artikujt_politike = artikulli.objects.filter(kategoria = 'Politike').order_by('-data')
    paginator_politike = Paginator(artikujt_politike, 8)
    politike_page_num = request.GET.get('politike_page', 1)
    artikujt_politike = paginator_politike.page(politike_page_num)

    artikujt_ekonomi = artikulli.objects.filter(kategoria = 'Ekonomi').order_by('-data')
    paginator_ekonomi = Paginator(artikujt_ekonomi, 8)
    ekonomi_page_num = request.GET.get('ekonomi_page', 1)
    artikujt_ekonomi = paginator_ekonomi.page(ekonomi_page_num)

    artikujt_opinion = artikulli.objects.filter(kategoria = 'Opinion').order_by('-data')
    paginator_opinion = Paginator(artikujt_opinion, 8)
    opinion_page_num = request.GET.get('opinion_page', 1)
    artikujt_opinion = paginator_opinion.page(opinion_page_num)

    artikujt_sporti = artikulli.objects.filter(kategoria = 'Sporti').order_by('-data')
    paginator_sporti = Paginator(artikujt_sporti, 8)
    sporti_page_num = request.GET.get('sporti_page', 1)
    artikujt_sporti = paginator_sporti.page(sporti_page_num)

    artikujt_kulture = artikulli.objects.filter(kategoria = 'Kulture').order_by('-data')
    paginator_kulture = Paginator(artikujt_kulture, 8)
    kulture_page_num = request.GET.get('kulture_page', 1)
    artikujt_kulture = paginator_kulture.page(kulture_page_num)

    sections = {'Aktualitet': artikujt_aktualitet, 'Politike': artikujt_politike, 'Ekonomi': artikujt_ekonomi, 'Opinion': artikujt_opinion, 'Sporti': artikujt_sporti, 'Kulture': artikujt_kulture}

    return render(request, 'Faqja_kryesore/home.html', {'sections': sections})
    

