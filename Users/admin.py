from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Users.models import CustomUser

admin.site.register(CustomUser, UserAdmin)
