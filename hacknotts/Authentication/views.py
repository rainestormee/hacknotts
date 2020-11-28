from django.shortcuts import render, HttpResponseRedirect

import random
from .forms import authCodeForm


# Create your views here.

def verification(request):
    random_number = random.randint(0, 16777215)
    hex = str(hex(random_number))
    authCode = '#' + hex

    print(authCode)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = authCodeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            authCodeRecieved = form.cleaned_data['auth code']
            if authCodeRecieved == authCode:
                request.user.
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = authCodeForm()

    return render(request, 'name.html', {'form': form})