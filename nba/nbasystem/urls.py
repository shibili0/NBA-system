from django.urls import path

from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login/',views.loginpage, name="loginpage"),
    path('register/',views.register, name="register"),
    path('logout/',views.logoutpage, name="logout"),
    path('shome/',views.shome, name="shome"),
    path('fhome/',views.fhome, name="fhome"),
    path('adminhome/',views.adminhome, name="adminhome"),
    path('phome/',views.phome, name="phome"),
    path('search/',views.search, name="search")
]