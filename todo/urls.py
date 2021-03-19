from django.contrib import admin
from django.urls import path,include
from .views import welcome,get_calendar_events,add_calendar_events,delete_calendar_events

urlpatterns = [
    path('welcome',welcome),
    path('add',add_calendar_events,name="add event"),
    path('get',get_calendar_events,name='get list of events'),
    path('delete',delete_calendar_events,name="Delete event")
]   