from django.contrib import admin
from django.urls import path

from django.urls import include

urlpatterns = [
    path('', include('main_page.urls')),
    path('admin/', admin.site.urls)
]
