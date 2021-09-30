from django.contrib import admin
from .models import NetworkDevice

# Register your models here.
@admin.register(NetworkDevice)
class NetworkDevice(admin.ModelAdmin):
    list_display = ('ip','hostname','device_model', 'pingable', 'version', 'updated')
    search_fields = ('version')
