from django.contrib import admin
from django.urls import path,include
from .views import welcome,CreateCalendarAPI,ModifyCalendarAPI

urlpatterns = [
    path('welcome',welcome),
    path('add',CreateCalendarAPI.as_view(),name="add event"),
    path('get/<int:pk>',ModifyCalendarAPI.as_view(),name='get list of events'),
    path('delete/<int:pk>',ModifyCalendarAPI.as_view(),name="Delete event")
]   