from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'test1/home.html')

def first(request):
    return render(request, 'test1/first.html')

def second(request):
    return render(request, 'test1/second.html') 
