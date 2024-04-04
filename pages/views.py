from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "homepage.html"

class AboutPageView(TemplateView): # new
    template_name = "about.html"

def homePageView(request):
    return HttpResponse("Hello, World!")

# Create your views here.
