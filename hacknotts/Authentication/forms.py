from django import forms
from .models import *

class authCodeForm(forms.Form):
    authCode = forms.CharField(label='auth code', max_length=100)

class bank_account_form(forms.ModelForm):
    class Meta:
        model = bank_account
        fields = ['accountID','telephoneNumber']