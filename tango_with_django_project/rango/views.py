from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")

def about(request):
	return HttpResponse("Rango Says: Here is the about page <a href='/rango'>Back</a>")