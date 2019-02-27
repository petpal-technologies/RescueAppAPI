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
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from PetPosts import views as petView
from Users import views
from django.conf.urls.static import static
from django.conf import settings



router = routers.DefaultRouter()

urlpatterns = [
    # url('auth/login/', obtain_auth_token, name='api_token_auth'),
    # url('accounts/', include('django.contrib.auth.urls')),
    # url('^accounts/', include('allauth.urls')),

    url('auth/login', views.auth_login),
    url('auth/logout', views.auth_logout),
    url('auth/signup', views.signup),


    url('api/new_post', csrf_exempt(petView.PostView.as_view())),
    url('api/delete', csrf_exempt(petView.PostView.as_view())),
    url('api/getPosts', csrf_exempt(petView.PostView.as_view())),


    url(r'^post/(?P<post_id>\d+)/$', petView.single_post_view, name='single_post_view'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
