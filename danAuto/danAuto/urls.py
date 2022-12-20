from django.contrib import admin
from django.urls import path

from django.urls import include
from main_page.views import *

urlpatterns = [
    path('', include('main_page.urls')),
    path('admin/', admin.site.urls)
]
