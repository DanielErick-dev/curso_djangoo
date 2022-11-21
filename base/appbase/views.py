from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('mensagem sendo enviada através da views do Django, matheus vire homem e pare de menstruar')
# Create your views here.
