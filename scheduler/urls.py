from django.conf.urls import include
from django.urls import path
from scheduler.views import AppointmentDetails, AppointmentDetailsChanges



urlpatterns = [
    path('', AppointmentDetails.as_view()),
    path('changes/<pk>', AppointmentDetailsChanges.as_view())
]