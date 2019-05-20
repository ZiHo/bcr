from bcrsystem.models import bookInfo,classroom
from django import forms
from django.contrib.auth.models import User


class BookInfoEditAdminForm(forms.ModelForm):
    class Meta:
        model = bookInfo
        fields = '__all__'

class ClassroomEditAdminForm(forms.ModelForm):
    class Meta:
        model = classroom
        fields = '__all__'

class UserEditAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['password', 'last_login', 'date_joined']

