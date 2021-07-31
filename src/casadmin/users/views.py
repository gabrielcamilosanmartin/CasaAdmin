from django.contrib.auth.views import LoginView
from .forms import UserCreationForm, UserEditForm
from .models import User
from casadmin.core.mixin import (DefaultListView, DefaultCreateView,
                                 DefaultEditView, DefaultDeleteView,
                                 DefaultDetailView)


class LoginView(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True


class UserList(DefaultListView):
    model = User
    icon = 'person'


class UserCreate(DefaultCreateView):
    model = User
    icon = 'person'
    form_class = UserCreationForm


class UserDelete(DefaultDeleteView):
    model = User


class UserEdit(DefaultEditView):
    model = User
    icon = 'person'
    form_class = UserEditForm


class UserDetail(DefaultDetailView):
    model = User
    icon = 'person'
