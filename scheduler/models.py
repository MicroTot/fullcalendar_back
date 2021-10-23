from django.db import models
from django.forms import ModelForm


# Create your models here.
class Appointment(models.Model):
    title = models.CharField(max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=20)
    


    class Meta:
        ordering = ("-id",)
    def __str__(self):
        return f"{self.title} session is beginning at {self.start}"




        # id: '1',
        #         start: addDays(startOfHour(new Date()), 1),
        #         end: addDays(addHours(startOfHour(new Date()), 1), 1),
        #         title: 'Event 1',
        #         content: 'IMPORTANT EVENT',
        #         color: { primary: '#E0E0E0', secondary: '#EEEEEE' },
        #         actions: actions,
        #         status: 'danger' as CalendarSchedulerEventStatus,
        #         isClickable: true,
        #         isDisabled: false,
        #         draggable: true,
        #         resizable: {
        #             beforeStart: true,
        #             afterEnd: true
        #         }
        #     },