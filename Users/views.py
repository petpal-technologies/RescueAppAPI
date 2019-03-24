from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

from . import serializers
from . import models


@csrf_exempt
def auth_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
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
        login(request,user)
        serializer = serializers.UserSerializer(user)
    else:
        u = models.CustomUser(username=request.POST['username'])
        u.set_password(request.POST['password'])
        u.save()
        login(request, u)
        serializer = serializers.UserSerializer(u)

    return JsonResponse(serializer.data)

def auth_logout(request):
    """Clears the session """
    logout(request)
    return HttpResponse(status=200)