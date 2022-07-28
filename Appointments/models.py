from django.db import models

# Create your models here.

class AppointmentType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=800, blank=True, null=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    type = models.ForeignKey(AppointmentType, on_delete=models.CASCADE)
    attendee_name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField()
    commence_time = models.DateTimeField()
    end_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
