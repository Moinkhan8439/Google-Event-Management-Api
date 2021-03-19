from rest_framework import serializers
from .models import Event
from .utils import connect_to_calendar,prepare_event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    def save(self,request,**validated_data):
        service=connect_to_calendar(request=request)
        event = prepare_event(validated_data)
        created_event = service.events().quickAdd(
        calendarId='primary',
        text=f'{event["summary"]} on Mar 19 12:33am-12:39am').execute()
        organizer=created_event['organizer']['email']
        id=created_event['id']
        keyword=self.validated_data['keyword']
        event=Event.objects.create(id=id,organizer=organizer,summary=txt,keyword=keyword)
        return event