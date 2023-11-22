# admin.py
from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(NewTodo)
admin.site.register(TodoGroup)