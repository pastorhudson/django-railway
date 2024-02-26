from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, 'home/home.html')
