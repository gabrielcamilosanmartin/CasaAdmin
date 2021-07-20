from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from casadmin.home.mixin import *


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'
    extra_context = {'segment': 'home', 'title': 'Dashboard'}
