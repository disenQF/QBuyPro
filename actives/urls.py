#!/usr/bin/python3
# coding: utf-8

from django.urls import path
from .views import ActiveGoodsView

app_name = 'activies'
urlpatterns = [
    path('info/',ActiveGoodsView.as_view(), name='info')
]