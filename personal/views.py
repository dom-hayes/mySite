from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def cv(request):    
    return render(request, "CV/cv.html")

def plfs(request):    
    return render(request, "PLFS/plfs.html")