from django.urls import path
from .views import *


urlpatterns = [
    path('bank/', BankList.as_view(), name='bankList'),
    path('bank/add', BankCreate.as_view(), name='bankCreate'),
    path('bank/delete/<pk>', BankDelete.as_view(), name='bankDelete'),
    path('bank/edit/<pk>', BankEdit.as_view(), name='bankEdit'),
    path('bank/detail/<pk>', BankDetail.as_view(), name='bankDetail'),

    path('', CredentialList.as_view(), name='credentialList'),
    path('add', CredentialCreate.as_view(), name='credentialCreate'),
    path('delete/<pk>', CredentialDelete.as_view(), name='credentialDelete'),
    path('edit/<pk>', CredentialEdit.as_view(), name='credentialEdit'),
    path('detail/<pk>', CredentialDetail.as_view(), name='credentialDetail'),

    path('account/', AccountList.as_view(), name='accountList'),
    path('account/add', AccountCreate.as_view(), name='accountCreate'),
    path('account/delete/<pk>', AccountDelete.as_view(), name='accountDelete'),
    path('account/edit/<pk>', AccountEdit.as_view(), name='accountEdit'),
    path('account/detail/<pk>', AccountDetail.as_view(), name='accountDetail'),

    path('accountType/', AccountTypeList.as_view(), name='accounttypeList'),
    path('accountType/add', AccountTypeCreate.as_view(), name='accounttypeCreate'),
    path('accountType/delete/<pk>', AccountTypeDelete.as_view(), name='accounttypeDelete'),
    path('accountType/edit/<pk>', AccountTypeEdit.as_view(), name='accounttypeEdit'),
    path('accountType/detail/<pk>', AccountTypeDetail.as_view(), name='accounttypeDetail'),
]
