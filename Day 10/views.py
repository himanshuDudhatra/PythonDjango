from myApp.models import Student
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.views.generic import ListView

# Create your views here.
def homePage(request):
    return HttpResponse("<h1>welocme home page</h1>")

def aboutPage(request):
    return HttpResponse("<h1>welocme about page</h1>")

class studentlist(ListView):
    model = Student
    template_name = "list.html"