from django.http import HttpResponse, request
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

def sum(request):
    return render(request,'sum.html')

def showData(request):
    a = request.GET['num1']
    b = request.GET['num2']
    c = a + b
    params = {"old1":a,"old2":b,"ans":c}
    return render(request,'showData.html',params)

def task8(request):
    return render(request,'form.html')

def formData(request):
    print(request)
    print(request.method)
    print(request.POST)
    a = request.POST['fname']
    b = request.POST['lname']
    c = request.POST['add']
    d = request.POST['Email']
    e = request.POST['password']
    dir = {"fname":a,"lname":b,"add":c,"Email":d,"password":e}
    return render(request,"formData.html",dir)