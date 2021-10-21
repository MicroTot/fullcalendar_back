from django.conf.urls import include
from django.urls import path
from scheduler.views import AppointmentDetails



urlpatterns = [
    path('', AppointmentDetails.as_view()),
    
]