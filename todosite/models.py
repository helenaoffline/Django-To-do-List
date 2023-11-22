# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class TodoGroup(models.Model):
    group=models.CharField(max_length=20)

    def __str__(self):
        return self.group

class NewTodo(models.Model):
    group=models.ForeignKey(TodoGroup,on_delete=models.CASCADE)
    name_todo=models.CharField(max_length=30)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.name_todo
   