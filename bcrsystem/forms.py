from django import forms
from django.contrib import auth


class LoginForm(forms.Form):
    username = forms.CharField(label='User', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))
    password = forms.CharField(label='Password', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('username or password error')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data
