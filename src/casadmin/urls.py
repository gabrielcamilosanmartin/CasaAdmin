from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('casadmin.home.urls')),
    path('', include('casadmin.user.urls')),
]
