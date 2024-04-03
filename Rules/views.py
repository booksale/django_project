from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Rules(request):
    return HttpResponse('<h1>Rules</h1>')