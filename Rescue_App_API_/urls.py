"""Rescue_App_API_ URL Configuration

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

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views as rest_framework_views

from rest_framework.authtoken.views import obtain_auth_token
from Users import views as Userview
from PetPosts import views as petView

urlpatterns = [
    url('hello/', Userview.HelloView.as_view(), name='hello'),
    url('auth/login/', obtain_auth_token, name='api_token_auth'),
    url('sayHi/', petView.SayHiBasic.as_view(), name="sayHi")

]