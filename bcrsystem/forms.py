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


class bookingForm(forms.Form):
    # classroom_type = forms.ChoiceField(label='')
    Type = forms.ChoiceField(
        initial=1,
        choices=((1, 'Normal'), (2, 'Lab')))

    Day = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))

    def clean_Day(self):
        day = self.cleaned_data['Day']
        return day

    def clean_Type(self):
        type1 = self.cleaned_data['Type']
        return type1
