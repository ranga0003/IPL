from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def warner(request):
    return render(request,'warner.html')

def bhuvi(request):
    return HttpResponse('<h1>swing king</h1>')
