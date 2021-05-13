from django.urls import path
from casadmin.home.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('hola', HomeView.as_view(),name='hola'),
]
