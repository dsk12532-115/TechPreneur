"""expert_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from expert.views.register import register_view, done_view

def index(request):
    contexts = {}
    return render(request,'index.html',contexts)

def give_form(request):
    contexts = {}
    return render(request,'give_form.html',contexts)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register_view, name='register'),
    path('accounts/register/done', done_view, name='register_done'),
    path('expert/', include('expert.urls')),
    # path('give_form/', give_form, name='give_form' ),
    # path('give_form/give', give, name="g_form"),
]
