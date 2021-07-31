from django.urls import path
from casadmin.core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('hola', HomeView.as_view(), name='hola'),
]
