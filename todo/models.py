from django.db import models
from django.utils.translation import gettext,gettext_lazy as _
from django.conf import settings
from allauth.socialaccount.models import SocialAccount


class Event(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE)
    Eid=models.CharField(_("Event id"), max_length=50,blank=True)
    summary=models.CharField(_("Title"), max_length=120)
    organizer=models.CharField(_("Organizer of event "), max_length=50,blank=True)
    start_time=models.DateTimeField(_("Event start time"), auto_now=False, auto_now_add=False)
    end_time=models.DateTimeField(_("Event end time"), auto_now=False, auto_now_add=False)
    description=models.CharField(_("Description"), max_length=200)
    attendees=models.CharField(_("Attendees"),default=" " ,max_length=1000,help_text="enter attendees separated by a comma ",blank=True)


    def __str__(self):
        return self.summary

