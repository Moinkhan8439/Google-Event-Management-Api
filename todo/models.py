from django.db import models
from django.utils.translation import gettext,gettext_lazy as _
from django.db.models.signals import post_save



class Event(models.Model):
    Eid=models.CharField(_("Event id"), max_length=50,blank=True)
    summary=models.CharField(_("Title"), max_length=120)
    organizer=models.CharField(_("Organizer of event "), max_length=50,blank=True)
    start_time=models.DateTimeField(_("Event start time"), auto_now=False, auto_now_add=False)
    end_time=models.DateTimeField(_("Event end time"), auto_now=False, auto_now_add=False)
    description=models.CharField(_("Description"), max_length=50)


    def __str__(self):
        return self.summary

