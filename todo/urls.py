from django.contrib import admin
from django.urls import path,include
from .views import api_overview,    ModifyCalendarAPI   ,   CreateCalendarAPI

urlpatterns = [
    path('',api_overview,name='Overview of API'),
    path('add/',CreateCalendarAPI.as_view(),name="Add Event"),
    path('list/',CreateCalendarAPI.as_view(),name="List of Event"),
    path('get/<int:pk>',ModifyCalendarAPI.as_view(),name='Get a Event'),
    path('delete/<int:pk>',ModifyCalendarAPI.as_view(),name="Delete event"),
    path('update/<int:pk>',ModifyCalendarAPI.as_view(),name="Update Event"),
]           