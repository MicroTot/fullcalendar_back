from django.shortcuts import render
from rest_framework import generics
from scheduler.models import Appointment
from scheduler.serializers import AppointmentSerializers

# Create your views here
class AppointmentDetails(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers

