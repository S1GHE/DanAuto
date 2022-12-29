from django.shortcuts import render, HttpResponse
from pathlib import Path


def main_page(request):
    return render(request, Path('main_page', 'index.html'))


def catalog(request):
    return HttpResponse('Данная страница пока недоступна')
