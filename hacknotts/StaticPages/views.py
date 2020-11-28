from django.shortcuts import render, HttpResponse, loader



# Create your views here.

def home(request):
    template = loader.get_template('StaticPages/home.html')
    context = { }
    return HttpResponse(template.render(context, request))


def tips(request):
    template = loader.get_template('StaticPages/tips.html')
    context = { }
    return HttpResponse(template.render(context, request))