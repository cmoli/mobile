# _*_ coding: utf-8 _*_ 
__author__ = 'Moli'
__date__ = '2020/1/1 13:52'

from django.contrib.auth.urls import path
from .admin import Admin


urlpatterns = [
    path('admin', Admin.as_view())
]