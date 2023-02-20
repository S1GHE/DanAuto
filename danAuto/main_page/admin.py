from django.contrib import admin
from .models import *


class NewOrderAdmin(admin.ModelAdmin):
    list_display = [
        'date_create_order',
        'name',
        'last_name',
        'middle_name',
        'telephone_number',
        'car_vin',
        'car_brand',
        'car_model',
        'car_year',
    ]

    search_fields = [
        'date_create_order',
        'name',
        'last_name',
        'middle_name',
        'telephone_number',
        'car_vin',
        'car_brand',
        'car_model',
        'car_year',
    ]


admin.site.register(NewOrder, NewOrderAdmin)
