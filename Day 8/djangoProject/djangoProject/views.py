from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
#def homePage(request):
    #return HttpResponse("welocme home page")

#def homePage(request):
 #   return render(request,'home.html')

#def aboutPage(request):
 #   return render(request,'about.html')

#def conatactPage(request):
 #   return render(request,'contact.html')

def home(request):
    return render(request,'index1.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def temFile(request):
    return render(request,'index.html')