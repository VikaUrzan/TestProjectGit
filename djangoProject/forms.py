from django import forms


class UserForm(forms.Form):
    login = forms.CharField()