from django.urls import path
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path('', views.LoginView.as_view(template_name='user/login.html')),
    path('index/', index, name="home")
]