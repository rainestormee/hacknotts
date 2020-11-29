from django.shortcuts import render, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .api import *


# Create your views here.
@login_required
def index2(request):
    content = ApiGet('https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts')
    return HttpResponse(content.text)


@login_required
def index(request):
    template = loader.get_template('WebApp/account.html')
    context = { }
    return HttpResponse(template.render(context, request))



