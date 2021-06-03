from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def homePage(request):
    return HttpResponse("welocme home page")

def homePage(request):
    return render(request,'home.html')

def aboutPage(request):
    return render(request,'about.html')

def conatactPage(request):
    return render(request,'contact.html')