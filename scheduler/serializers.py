from rest_framework import serializers
from scheduler.models import Appointment


class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)