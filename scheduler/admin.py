from django.contrib import admin
from scheduler.models import Appointment

# Register your models here.
admin.site.register(Appointment)
admin.site.site_header  =  "Pesapal Scheduler Admin" 