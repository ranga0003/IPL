from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def rohit(request):
    return render(request,'rohit.html')

def kishan(request):
    return HttpResponse('<h1>left hand batsman</h1>')
