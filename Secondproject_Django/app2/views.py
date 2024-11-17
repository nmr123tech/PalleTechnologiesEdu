from django.shortcuts import render

# Create your views here.



def home(request):
    return HttpResponse(f"<h1>welcome to app2</h1>")