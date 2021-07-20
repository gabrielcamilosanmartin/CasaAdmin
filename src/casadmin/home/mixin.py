from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class DefaultCRUD(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # define name of model
        context['verbose_name_plural'] = context['title'] = self.model._meta.verbose_name_plural
        context['verbose_name'] = self.model._meta.verbose_name
        # define segment for nav menu
        context['segment'] = self.model._meta.model_name
        #define icon for title
        context['icon'] = self.icon if hasattr(self, 'icon') else ''
        #define namespace of link fro CRUD 

        context['url'] = {
            'list' : self.model._meta.model_name + 'List',
            'detail' : self.model._meta.model_name + 'Detail',
            'create' : self.model._meta.model_name + 'Create',
            'edit' : self.model._meta.model_name + 'Edit',
            'delete' : self.model._meta.model_name + 'Delete',
            }
        return context


class DefaultListView(DefaultCRUD, ListView):
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs) 
        context['order_by'] = self.request.GET.get('order-by', 'id')
        return context

    def get_ordering(self):
        return self.request.GET.get('order-by', 'id')

    def get_template_names(self):
        return self.model._meta.model_name + '/list.html'


class DefaultCreateView(SuccessMessageMixin, DefaultCRUD, CreateView):

    def get_success_message(self, form):
        return self.model._meta.verbose_name.title() + " creado con exito"
        
    def get_template_names(self):
        return self.model._meta.model_name + '/create.html'
    
    def get_success_url(self):
        return reverse_lazy(self.model._meta.model_name + 'List')


class DefaultEditView(SuccessMessageMixin, DefaultCRUD, UpdateView):

    def get_success_message(self, form):
        return self.model._meta.verbose_name.title() + " modificado con exito"
        
    def get_template_names(self):
        return self.model._meta.model_name + '/edit.html'
    
    def get_success_url(self):
        return reverse_lazy(self.model._meta.model_name + 'List')

class DefaultDetailView(DefaultCRUD, DetailView):
    def get_template_names(self):
        return self.model._meta.model_name + '/detail.html'


class DefaultDeleteView(DeleteView, DefaultCRUD):

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.model._meta.verbose_name.title() + " eliminado con exito")
        return super(DefaultDeleteView, self).delete(request, *args, **kwargs)

    def get_success_message(self, form):
        print ('*******************************')
        return self.model._meta.verbose_name.title() + " eliminado con exito"
    
    def get_success_url(self):
        return reverse_lazy(self.model._meta.model_name + 'List')
