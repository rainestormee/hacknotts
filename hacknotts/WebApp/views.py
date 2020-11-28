from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .api import *

# Create your views here.

def email_check(user):
    return user.email.endswith('@example.com')

@login_required
@user_passes_test(email_check)
def index(request):
    content = ApiGet('https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts')
    return HttpResponse(content.text)





