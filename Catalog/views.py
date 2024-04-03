from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Catalog(request):
    return HttpResponse('<h1>Catalog</h1>')
