from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from twilio.rest import Client
import random

from .forms import authCodeForm, bank_account_form
from .models import *
from .api import ApiGet


# Create your views here.
@login_required
def verification(request):


    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = authCodeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            authCodeRecieved = form.cleaned_data['auth code']
            for account in bank_account.objects.filter(user=request.user):
                if authCodeRecieved == account.authCode:
                    account.verified = True
                    account.save()
            return HttpResponseRedirect(' ')

    # if a GET (or any other method) we'll create a blank form
    else:
        account_sid = 'AC981838466c123165f5a99c5913488181'
        auth_token = 'f33080514f1b3e9cd3b7c6e6dc92748b'
        messaging_sid = '+447477579378'  # 'PN77be9d18bceff01b2e184040f98c516e'
        accounts = bank_account.objects.filter(user=request.user)
        for account in accounts:
            the_body = str(account.authCode)
        try:
            client = Client(account_sid, auth_token)
            client.messages.create(
                to='+447477579378',  # self.phone_number,
                from_=messaging_sid,
                body=(f"Authorization Code: {the_body}")
            )

        except Client.TwilioRestException as err:
            print(err)

        form = authCodeForm()

    return render(request, 'Authentication/verification.html', {'form': form})

@login_required
def bank_account_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = bank_account_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            apiResult=ApiGet("https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts/" + str(form.cleaned_data['accountID']))
            apiResult = apiResult.json()
            apiResult = apiResult['Accounts'][0]
            print(apiResult['phoneNumber'])
            print(form.cleaned_data['telephoneNumber'])
            if apiResult['phoneNumber'] == ("+" + str(form.cleaned_data['telephoneNumber'])):
                bank_account_instance = bank_account.objects.create(user = request.user,
                                                                    accountID = form.cleaned_data['accountID'],
                                                                    verified=False,
                                                                    telephoneNumber = form.cleaned_data['telephoneNumber'],
                                                                    authCode = random.randint(0, 99999))
                bank_account_instance.save()
                return HttpResponseRedirect('/accounts/verification/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = bank_account_form()

    return render(request, 'Authentication/associate_bank_account.html', {'form': form})

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect(' ')
    context['form']=form
    return render(request,'registration/sign_up.html',context)
