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
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from PetPosts import views as petView
from django.conf.urls.static import static
from django.conf import settings
from Comments import views as commentView
from Users import views as userView


router = routers.DefaultRouter()

urlpatterns = [

    url('auth/login', userView.auth_login),
    url('auth/logout', userView.auth_logout),
    url('auth/signup', userView.signup),


    url('api/new_post', csrf_exempt(petView.PostView.as_view())),
    url('api/delete', csrf_exempt(petView.PostView.as_view())),
    url('api/getPosts', csrf_exempt(petView.PostView.as_view())),
    url('api/editPost', csrf_exempt(petView.PostView.as_view())),


    url(r'^post/(?P<post_id>[0-9a-f-]+)/$', petView.single_post_view, name='single_post_view'),
    url(r'comments', commentView.LoginView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
