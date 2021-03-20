from rest_framework import serializers
from .models import Event
from .utils import connect_to_calendar,prepare_event
from rest_framework.response  import Response

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    def save(self,request):
        service=connect_to_calendar(request=request)
        event = prepare_event(self.validated_data)
        created_event = service.events().insert(calendarId='primary', body=event).execute()
        self.validated_data['organizer']=created_event['organizer']['email']
        self.validated_data['Eid']=created_event['id']
        event=Event.objects.create(self.validated_data)
        return event
    
    def update(self,instance):
        pass

    def delete(self):
        id=self.kwargs['pk']
        event=Event.objects.filter(id=id)
        service=connect_to_calendar(request=self.request)
        service.events().delete(calendarId='primary', eventId=event['Eid']).execute()
        event.delete()
        msg={"detail":"deleted successfully"}
        return msg