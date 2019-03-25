from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

from . import serializers
from . import models
from Rescue_App_API_ import settings


@csrf_exempt
def auth_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    return JsonResponse("USER: "+user)

    if user:
        login(request, user, backend=settings.AUTH_USER_MODEL)
        serializer = serializers.UserSerializer(user)
        return JsonResponse(serializer.data)
    return HttpResponse(status=401)


@csrf_exempt
def signup(request):
    if models.CustomUser.objects.filter(username=request.POST['username']).exists():
        # Login the user if username exists
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user, backend=settings.AUTH_USER_MODEL)
        serializer = serializers.UserSerializer(user)
    else:
        u = models.CustomUser(username=request.POST['username'], user_name=request.POST['user_name'])
        u.set_password(request.POST['password'])
        u.save()
        login(request, u, backend=settings.AUTH_USER_MODEL)
        serializer = serializers.UserSerializer(u)

    return JsonResponse(serializer.data)

def auth_logout(request):
    """Clears the session """
    logout(request)
    return HttpResponse(status=200)