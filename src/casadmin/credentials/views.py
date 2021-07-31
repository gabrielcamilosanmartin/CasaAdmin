from .models import Bank, Credential, Account, AccountType
from casadmin.core.mixin import (DefaultListView, DefaultCreateView,
                                 DefaultEditView, DefaultDeleteView,
                                 DefaultDetailView)


class BankList(DefaultListView):
    model = Bank
    icon = 'account_balance'


class BankCreate(DefaultCreateView):
    model = Bank
    icon = 'account_balance'


class BankDelete(DefaultDeleteView):
    model = Bank


class BankEdit(DefaultEditView):
    model = Bank
    icon = 'account_balance'


class BankDetail(DefaultDetailView):
    model = Bank
    icon = 'account_balance'


class CredentialList(DefaultListView):
    model = Credential
    icon = 'vpn_key'


class CredentialCreate(DefaultCreateView):
    model = Credential
    icon = 'vpn_key'


class CredentialDelete(DefaultDeleteView):
    model = Credential


class CredentialEdit(DefaultEditView):
    model = Credential
    icon = 'vpn_key'


class CredentialDetail(DefaultDetailView):
    model = Credential
    icon = 'vpn_key'


class AccountList(DefaultListView):
    model = Account
    icon = 'credit_card'


class AccountCreate(DefaultCreateView):
    model = Account
    icon = 'credit_card'


class AccountDelete(DefaultDeleteView):
    model = Account


class AccountEdit(DefaultEditView):
    model = Account
    icon = 'credit_card'


class AccountDetail(DefaultDetailView):
    model = Account
    icon = 'credit_card'


class AccountTypeList(DefaultListView):
    model = AccountType
    icon = 'credit_card'


class AccountTypeCreate(DefaultCreateView):
    model = AccountType
    icon = 'credit_card'


class AccountTypeDelete(DefaultDeleteView):
    model = AccountType


class AccountTypeEdit(DefaultEditView):
    model = AccountType
    icon = 'credit_card'


class AccountTypeDetail(DefaultDetailView):
    model = AccountType
    icon = 'credit_card'