import re
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class NameValidator(validators.RegexValidator):
    regex = r'^[\w .-]+\Z'
    message = _(
        'Enter a valid bank name. This value may contain only letters, '
        'numbers, and /./- characters.'
    )
    flags = 0


@deconstructible
class UrlValidator(validators.RegexValidator):
    regex = r'^(https?:\/\/)?[\w\-]+(\.[\w\-]+)+[/#?]?.*$'
    message = _('Enter a valid URL')
    flags = 0
