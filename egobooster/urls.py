# egobooster/urls.py
from django.urls import path
from .views import my_tkinter_view

urlpatterns = [
    path('', my_tkinter_view, name='tkinter_view'),
]
