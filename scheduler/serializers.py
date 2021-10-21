from rest_framework import serializers
from scheduler.models import Appointment


class AppointmentSerializers(serializers.ModelSerializer):
    def validate(self, obj):
        data = self.get_initial()
        start = obj['start']
        end = obj['end']
        title = obj['title']
        
        time_in_duplicate = Appointment.objects.filter(start__day=start.day, start__hour=start.hour)
        if time_in_duplicate.exists():
            raise serializers.ValidationError("That room is booked already!")

        time_out_duplicate = Appointment.objects.filter(end__day=end.day, end__hour=end.hour)
        if time_out_duplicate.exists():
            raise serializers.ValidationError("That room is booked already!")
        return super(AppointmentSerializers, self).validate(obj)

    class Meta:
        model = Appointment
        fields = [
            "start",
            "end",
            "title",
        ]

    