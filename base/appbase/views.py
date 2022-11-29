from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(' seja bem vindo ')

# Create your views here.
