from django import forms


class BaseForm(forms.ModelForm):

    class Meta:
        exclude = ('deleted_at')