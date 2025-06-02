from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Hello from API") 
