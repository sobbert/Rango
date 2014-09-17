from django.shortcuts import render

# Create your views here.
from django.htpp import HttpResponse

def index(request):
	return HttpResponse("Rango says hello world!")