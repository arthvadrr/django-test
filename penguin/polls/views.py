from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("At polls index.")# Create your views here.
