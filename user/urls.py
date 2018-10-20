"""python_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name='user'
urlpatterns = [
    url(r'^login/', views.login,name='login'),
    # url(r'^show/(?P<myid>\w*)', views.show,name='show'),
    url(r'^regist/', views.regist,name='regist'),
    # url(r'^insert/', views.insert,name='insert'),
    url(r'^getuser/', views.getuser,name='getuser'),
    url(r'^index_users/', views.index_users,name='index_users'),
    url(r'^getcity/', views.getcity,name='getcity'),
    url(r'^getfilm/', views.getfilm,name='getfilm'),
    url(r'^getfood/', views.getfood,name='getfood'),
    url(r'^getpet/', views.getpet,name='getpet'),
    url(r'^get90/', views.get90,name='get90'),
    url(r'^search_users/', views.search_users,name='search_users'),
    url(r'^btn_search/', views.btn_search,name='btn_search'),
    url(r'^getuserAll/', views.getuserAll,name='getuserAll'),
]
