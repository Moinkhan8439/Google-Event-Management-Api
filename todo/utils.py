from datetime import datetime
import json
from allauth.socialaccount.models import SocialAccount,SocialToken
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from django.contrib.auth.models import User


def connect_to_calendar(request):
    qs=SocialAccount.objects.filter(user=request.user)
    token=SocialToken.objects.filter(account=qs[0]).values('token')
    SCOPES = ['https://www.googleapis.com/auth/calendar.events']
    creds = Credentials(token[0]['token'],SCOPES )
    service = build('calendar', 'v3', credentials=creds)
    return service





def convert_date(date):
    d=date.isoformat('T')
    print(d)
    return d



def prepare_event(data):
    start=convert_date(data['start_time'])
    end=convert_date(data['end_time'])
    event = {
        'summary': data['summary'],
        'description': data['description'],
        'start': {
            'dateTime': start,
            'timeZone': 'ASIA/KOLKATA',
        },
        'end': {
            'dateTime': end,
            'timeZone': 'ASIA/KOLKATA',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': 'moinkhan8439@gmail.com'},
            {'email': 'zainkhanjune@gmail.com'},
            ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        }
    }
    return json.dumps(event)

