from django.shortcuts import render, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .api import *
from django.apps import apps


# Create your views here.
@login_required
def index2(request):
    content = ApiGet('https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts')
    return HttpResponse(content.text)


@login_required
def index(request):
    bank_account = apps.get_model('Authentication', 'bank_account')
    template = loader.get_template('WebApp/account.html')
    context = {}
    for account in bank_account.objects.filter(user = request.user, verified = True):

        apiResult = ApiGet("https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/transactions/accounts/" + str(account.accountID) + "/transactions")
        transactions = apiResult.json()['Transactions']
        transactions_list = []

        for transaction in transactions:
            transaction_list = []
            transaction_list.append(transaction['merchant']['name'])
            transaction_list.append(transaction['amount'])
            transaction_list.append(transaction['message'])
            transaction_list.append(transaction['timestamp'])
            transaction_list.append(transaction['status'])
            transactions_list.append(transaction_list)

        context = {'transactions_list':transactions_list}
    return HttpResponse(template.render(context, request))



