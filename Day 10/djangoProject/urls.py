"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('myApp.urls')),
    #path("about",include('myApp.urls')),
    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="about"),
    path("tempFile",views.temFile,name="tempFile"),
    path("sum",views.sum,name="sum"),
    path("showData",views.showData,name="showData"),
    path("form",views.task8,name="form"),
    path("formData",views.formData,name="formData")
]
