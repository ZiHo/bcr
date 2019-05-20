from bcrsystem.models import bookInfo,classroom
from django import forms


class BookInfoEditAdminForm(forms.ModelForm):
    class Meta:
        model = bookInfo
        fields = '__all__'

class ClassroomEditAdminForm(forms.ModelForm):
    class Meta:
        model = classroom
        fields = '__all__'