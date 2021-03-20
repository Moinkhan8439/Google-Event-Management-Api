import datetime

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes,parser_classes
#from rest_framework.mixin import 
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from allauth.socialaccount.models import SocialAccount,SocialToken
from django.contrib.auth.models import User
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

from .serializers import EventSerializer,Event
from .utils import connect_to_calendar



# Create your views here.
@api_view(['GET'])
def welcome(request):
    return Response('hello')





class CreateCalendarAPI(ListCreateAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer


    def perform_create(self,serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save(request=self.request)


class ModifyCalendarAPI(RetrieveUpdateDestroyAPIView):
    serializer_class=EventSerializer
    queryset=Event.objects.all()
    

        

'''
@api_view(['GET'])
def get_calendar_events(request):
    qs=SocialAccount.objects.filter(user=request.user)
    token=SocialToken.objects.filter(account=qs[0]).values('token')
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = Credentials(token[0]['token'],SCOPES )
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.now().isoformat() + 'Z'
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=20, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    return Response(events)


@api_view(['DELETE'])
def delete_calendar_events(request,pk):
    event=Event.objects.all().values('id')
    qs=SocialAccount.objects.filter(user=request.user)
    token=SocialToken.objects.filter(account=qs[0]).values('token')
    creds = Credentials(token[0]['token'],SCOPES )
    service = build('calendar', 'v3', credentials=creds)
    service.events().delete(calendarId='primary', eventId=event['Eid']).execute()
    event.delete()
    return Response("student deleted successfully !!")




    qs=SocialAccount.objects.filter(user=request.user)
    token=SocialToken.objects.filter(account=qs[0]).values('token')
    print(token)
    SCOPES = ['https://www.googleapis.com/auth/calendar.events']
    creds = Credentials(token[0]['token'],SCOPES )
    service = build('calendar', 'v3', credentials=creds)
    created_event = service.events().quickAdd(
    calendarId='primary',
    text='Appointment at Somewhere on June 3rd 10am-10:25am').execute()
    print(created_event)
'''