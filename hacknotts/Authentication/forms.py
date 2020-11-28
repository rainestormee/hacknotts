from django import forms

class authCodeForm(forms.Form):
    authCode = forms.CharField(label='auth code', max_length=100)