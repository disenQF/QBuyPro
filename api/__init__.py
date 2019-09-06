#!/usr/bin/python3
# coding: utf-8
from rest_framework import routers

from .user import UserAPIView

# 声明api路由
api_router = routers.DefaultRouter()

# 向api路由中注册ViewSet
api_router.register('users', UserAPIView)
