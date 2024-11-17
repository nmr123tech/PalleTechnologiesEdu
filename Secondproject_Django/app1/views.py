from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse(f"<h1>welcome to apps</h1>")



def color_home(request):
    return HttpResponse(f"<h1 style'color:green'>welcome to apps</h1>")