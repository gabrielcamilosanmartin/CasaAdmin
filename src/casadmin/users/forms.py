from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'password'
            ]
