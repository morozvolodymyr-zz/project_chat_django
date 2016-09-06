from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(max_length=20, label='Login')
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
