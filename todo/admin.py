from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):

    def has_add_permission(self,request):
        return False
    


admin.site.register(Event)
