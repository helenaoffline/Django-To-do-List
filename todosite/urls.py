from django.urls import is_valid_path
from django.urls import path
from .views import *


urlpatterns = [
    path("home", NewTodoListView.as_view(), name="home"),
    path("delete/<int:pk>/",NewTodoDeleteView.as_view(),name="tododelete"),
    path("updade/<int:pk>/", NewTodoUpdateView.as_view(),name="todoupdate"),
    path("create/",NewTodoCreateView.as_view(),name="todocreate"),
    path("", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
]