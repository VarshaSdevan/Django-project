from django.contrib import admin

# Register your models here.

from .models import Event,Venue
admin.site.register(Venue)
#admin.site.register(MyClubUser)
admin.site.register(Event)

