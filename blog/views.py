from django.shortcuts import render
from blog.models import Entry, Practice

# Create your views here.

def index(request):
    return HttpResponse("Este es la app del proyecto")