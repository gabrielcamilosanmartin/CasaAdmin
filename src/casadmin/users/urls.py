from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (LoginView, UserList, UserCreate, UserDelete, UserEdit,
                    UserDetail)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', UserList.as_view(), name='userList'),
    path('add', UserCreate.as_view(), name='userCreate'),
    path('delete/<pk>', UserDelete.as_view(), name='userDelete'),
    path('edit/<pk>', UserEdit.as_view(), name='userEdit'),
    path('detail/<pk>', UserDetail.as_view(), name='userDetail'),
]
