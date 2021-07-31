from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView
    )


class DefaultCRUD(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Define name of model
        context['title'] = self.model._meta.verbose_name_plural
        context['verbose_name_plural'] = context['title']
        context['verbose_name'] = self.model._meta.verbose_name
        # Define segment for nav menu
        context['segment'] = self.model._meta.model_name
        # Define icon for title
        context['icon'] = self.icon if hasattr(self, 'icon') else ''
        # Define namespace of link fro CRUD

        context['url'] = {
            'list': self.model._meta.model_name + 'List',
            'detail': self.model._meta.model_name + 'Detail',
            'create': self.model._meta.model_name + 'Create',
            'edit': self.model._meta.model_name + 'Edit',
            'delete': self.model._meta.model_name + 'Delete',
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
    fields = '__all__'

    def get_success_message(self, form):
        return self.model._meta.verbose_name.title() + " creado con exito"

    def get_template_names(self):
        return self.model._meta.model_name + '/create.html'

    def get_success_url(self):
        return reverse_lazy(self.model._meta.model_name + 'List')

    def get_form_class(self):
        form = super(DefaultCreateView, self).get_form_class()
        form.base_fields.pop('deleted_at')
        return form


class DefaultEditView(SuccessMessageMixin, DefaultCRUD, UpdateView):
    fields = '__all__'

    def get_success_message(self, form):
        return self.model._meta.verbose_name.title() + " modificado con exito"

    def get_template_names(self):
        return self.model._meta.model_name + '/edit.html'

    def get_success_url(self):
        return reverse_lazy(self.model._meta.model_name + 'List')

    def get_form_class(self):
        form = super(DefaultEditView, self).get_form_class()
        form.base_fields.pop('deleted_at')
        return form


class DefaultDetailView(DefaultCRUD, DetailView):
    def get_template_names(self):
        return self.model._meta.model_name + '/detail.html'


class DefaultDeleteView(DeleteView, DefaultCRUD):

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            self.model._meta.verbose_name.title() + " eliminado con exito1")
        return super(DefaultDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(self.model._meta.model_name + 'List')
