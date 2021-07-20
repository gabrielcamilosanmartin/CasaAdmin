from django.contrib.auth.models import AbstractUser
from casadmin.home.models import SoftDeletionModelUser

class User(AbstractUser, SoftDeletionModelUser):
    pass