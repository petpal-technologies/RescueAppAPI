from django.urls import path

from . import views

from django.urls import path

from Users import views

urlpatterns = [
    path('login', views.auth_login),
    path('logout', views.auth_logout),
    path('signup', views.signup),
]