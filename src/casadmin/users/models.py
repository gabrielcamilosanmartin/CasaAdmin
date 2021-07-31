from django.contrib.auth.models import AbstractUser
from casadmin.core.models import SoftDeletionModelBase


class User(SoftDeletionModelBase, AbstractUser):
    pass
