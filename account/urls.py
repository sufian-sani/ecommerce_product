from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', customerlogin, name='login'),
]