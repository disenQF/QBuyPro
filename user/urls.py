#!/usr/bin/python3
# coding: utf-8
from django.urls import path

from .views import LoginView

from .views import user_api, user_api_detail, UserAPIView

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('api/', UserAPIView.as_view(), name='api'),
    path('api/<int:pk>', user_api_detail, name='api_detail')
]