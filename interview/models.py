from django.db import models
from django.contrib.auth.models import User
import datetime


class Interview(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SlotOption(models.Model):
    SLOT_CHOICES = (
        ('slot1', '9AM-10AM'),
        ('slot2', '10AM-11AM'),
        ('slot3', '11AM-12PM'),
        ('slot4', '12PM-1PM'),
        ('slot5', '1PM-2PM'),
        ('slot6', '2PM-3PM'),
        ('slot7', '3PM-4PM'),
        ('slot8', '4PM-5PM'),
        ('slot9', '5AM-6PM'),
    )
    sc = models.CharField(max_length=5, choices=SLOT_CHOICES)
    
    def __str__(self):
        return self.sc

class Slot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    date = models.DateField(default = datetime.date.today())
    choices = models.ManyToManyField(SlotOption)

    def __str__(self):
        return self.user.username
