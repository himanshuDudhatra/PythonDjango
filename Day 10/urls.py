from django.urls import path
from . import views

urlpatterns = [
    path("",views.homePage,name="home"),
    path("about",views.aboutPage,name="about"),
    path("list",views.studentlist.as_view(),name="list")
]
