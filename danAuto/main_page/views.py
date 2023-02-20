from django.shortcuts import render, HttpResponse, redirect
from pathlib import Path

from .forms import *


def main_page(request):
    if request.method == 'POST':
        new_order_form = AddNewOrder(request.POST)
        if new_order_form.is_valid():
            print(new_order_form.cleaned_data)

        try:
            new_order_form.save()
            return redirect('main_page')
        except Exception as error:
            print(error)
    else:
        new_order_form = AddNewOrder()

    return render(request, Path('main_page', 'index.html'), context={
        'form': new_order_form
    })


def catalog(request):
    return HttpResponse(request, 'Данная страница пока недоступна')
