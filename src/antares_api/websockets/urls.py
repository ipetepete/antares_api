from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.user_list, name="user_list")
]
