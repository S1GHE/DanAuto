from django.shortcuts import render
from pathlib import Path


def main_page(request):
    return render(request, Path('main_page', 'index.html'))
