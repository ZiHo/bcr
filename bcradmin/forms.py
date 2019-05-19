from bcrsystem.models import bookInfo
from django import forms


class BookInfoEditAdminForm(forms.ModelForm):
    class Meta:
        model = bookInfo
        fields = '__all__'
