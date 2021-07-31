from casadmin.core.models import SoftDeletionModelBase
from django.db import models
from casadmin.users.models import User
from .validators import (NameValidator, UrlValidator)
from django.utils.translation import gettext_lazy as _


class Bank(SoftDeletionModelBase):

    name_validator = NameValidator()

    name = models.CharField(
        _('name'),
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        help_text=_("Required. 50 characters or fewer. Letters and digits and"
                    " /./- only."),
        validators=[name_validator],
        error_messages={
            'unique': _("A bank with that name already exists."),
            'null': _('This field cannot be null.'),
            'blank': _('This field is required.'),
            },
        )

    class Meta:
        verbose_name = _('Bank')
        verbose_name_plural = _('Banks')

    def __str__(self):
        return self.name


class Credential(SoftDeletionModelBase):

    url_validator = UrlValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Required. 150 characters or fewer."),
        error_messages={
            'null': _('This field cannot be null.'),
            'blank': _('This field is required.'),
            },
        )

    password = models.CharField(
        _('password'),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Required. 150 characters or fewer."),
        error_messages={
            'null': _('This field cannot be null.'),
            'blank': _('This field is required.'),
            },
        )

    login_url = models.CharField(
        _('login URL'),
        help_text=_("Required. 500 characters or fewer."),
        max_length=500,
        null=False,
        blank=False,
        validators=[url_validator],
        error_messages={
            'null': _('This field cannot be null.'),
            'blank': _('This field is required.'),
            },
        )

    class Meta:
        verbose_name = _('Credential')
        verbose_name_plural = _('Credentils')

    def __str__(self):
        return self.login_url + ' : ' + self.username


class AccountType(SoftDeletionModelBase):

    name_validator = NameValidator()

    name = models.CharField(
        _('name'),
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        help_text=_("Required. 150 characters or fewer."),
        validators=[name_validator],
        error_messages={
            'unique': _("A type of bank account with that name"
                        "already exists."),
            'null': _('This field cannot be null.'),
            'blank': _('This field is required.'),
            },
        )

    class Meta:
        verbose_name = _('bank account type')
        verbose_name_plural = _('types of bank accounts')

    def __str__(self):
        return self.name


class Account(SoftDeletionModelBase):

    name_validator = NameValidator()

    name = models.CharField(
        _('name'),
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        help_text=_("Required. 150 characters or fewer."),
        validators=[name_validator],
        error_messages={
            'unique': _("A bank account with that name already exists."),
            'null': _('This field cannot be null.'),
            'blank': _('This field is required.'),
            },
        )

    balance = models.IntegerField(
        _('balance'),
        null=False,
        blank=False,
        default=0,
        error_messages={
            'null': _('This field cannot be null.'),
            'blank': _('This field is required.'),
            },
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name=_('User'))

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE,
                             verbose_name=_('Bank'))

    credential = models.ForeignKey(Credential, on_delete=models.CASCADE,
                                   verbose_name=_('Credential'))

    class Meta:
        verbose_name = _('Type of Account')
        verbose_name_plural = _('Types of Acounts')

    def __str__(self):
        return self.name
