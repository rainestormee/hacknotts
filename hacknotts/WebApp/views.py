from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .api import *
from ..Authentication.models import *

# Create your views here.
@login_required
def index(request):
    content = ApiGet('https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts')
    return HttpResponse(content.text)





