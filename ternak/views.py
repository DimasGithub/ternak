from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from vendor.models import hewan
from register.models import UserProfile
from django.core.paginator import Paginator
def index(request):       
    card = hewan.objects.all()
    paginator = Paginator(card, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'title':'BukaTernak',
        'header':'Welcome to e-commerce online BukaTernak',
        'cards':card,
        'page_obj':page_obj,
    }
    return render(request, 'index.html', context )
def indexCat(request,cat):
    card = hewan.objects.filter(kategori=cat)
    paginator = Paginator(card, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'title':'BukaTernak',
        'header':'Welcome to e-commerce online BukaTernak',
        'cards':card,
        'page_obj':page_obj,
    }
    return render(request, 'index.html', context )
# def indexSearch(request,key):
#     hewan.objects.filter(Q(title__icontains=key)|Q(body__icontains=key))
#     paginator = Paginator(card, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context={
#         'title':'BukaTernak',
#         'header':'Welcome to e-commerce online BukaTernak',
#         'cards':card,
#         'page_obj':page_obj,
#     }
#     return render(request, 'index.html', context )
