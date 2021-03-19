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


def prepare_event(data):
    print(data)
    event = {
        'summary': data['summary'],
        'description': data['description'],
        'start': {
            'dateTime': '2015-05-28T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2015-05-28T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': 'lpage@example.com'},
            {'email': 'sbrin@example.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
    }