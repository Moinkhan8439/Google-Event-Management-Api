from django.shortcuts                   import render
from .serializers                       import EventSerializer  ,   Event
from .utils                             import connect_to_calendar

from rest_framework.response            import  Response
from rest_framework.decorators          import  api_view
from rest_framework.generics            import  RetrieveUpdateDestroyAPIView    ,      ListCreateAPIView
from rest_framework.permissions         import  IsAuthenticated




# Create your views here.
@api_view(['GET'])
def api_overview(request):
    Overview={
        'Add these endpoints just after base url                    '  :                'https://calendar-assistance.herokuapp.com/',
        'For login                                                  '  :                'accounts/google/login/',
        'for logout                                                 '  :                'accounts/google/logout',
        'To get list of Events  REQUEST-TYPE = GET                  '  :                'get-list/',
        'Adding an Event  REQUEST-TYPE = POST                       '  :                'add/',
        'Detail of single Event  REQUEST-TYPE = GET                 '  :                'get/<int:pk>/',
        'Deleting an Event  REQUEST-TYPE = DELETE                   '  :                'update/<int:pk>/',
        'Updating a single Event REQUEST-TYPE = PUT OR PATCH        '  :                '/delete/<int:pk>/',
    }
    return Response(Overview)





class CreateCalendarAPI(ListCreateAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save_as(request=self.request)





class ModifyCalendarAPI(RetrieveUpdateDestroyAPIView):
    serializer_class=EventSerializer
    queryset=Event.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_update(self,serializer):
        serializer.update_as(request=self.request)
        instance=serializer.save()

    def perform_destroy(self,instance):
        service=connect_to_calendar(request=self.request)
        instance.delete()
        service.events().delete(calendarId='primary', eventId=instance.Eid).execute()
        msg={
            "event" : instance.summary,
            "detail":"deleted successfully",
            }
        return Response(msg)
        

        

