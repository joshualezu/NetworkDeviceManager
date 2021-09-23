from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# Create your models here.
class NetworkDevice(models.Model):
    default_date = datetime(2001,1,1,1,0,0,0)


    ip = models.CharField(max_length=50, unique=True)
    hostname = models.CharField(max_length=50)
    pingable = models.BooleanField(default=False)
    last_ping = models.DateTimeField(default=default_date)
    device_model = models.CharField(max_length=50, blank=True, null=True, default=None)
    serial_1 = models.CharField(max_length=11, blank=True, null=True, default=None)
    serial_2 = models.CharField(max_length=11, blank=True, null=True, default=None)
    serial_3 = models.CharField(max_length=11, blank=True, null=True, default=None)
    serial_4 = models.CharField(max_length=11, blank=True, null=True, default=None)
    serial_5 = models.CharField(max_length=11, blank=True, null=True, default=None)
    serial_6 = models.CharField(max_length=11, blank=True, null=True, default=None)
    serial_7 = models.CharField(max_length=11, blank=True, null=True, default=None)
    serial_8 = models.CharField(max_length=11, blank=True, null=True, default=None)
    serial_9 = models.CharField(max_length=11, blank=True, null=True, default=None)
    note = models.CharField(max_length=100, blank=True, null=True, default=None)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('pingable', 'ip')
    
    def __str__(self):
        return self.hostname

    def get_absolute_url(self):
        return reverse('device_detail',
                        args=[self.pk,self.ip])
