from django.contrib import admin
from .models import Location, Participant, Meetup

admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Meetup)
# Register your models here.
