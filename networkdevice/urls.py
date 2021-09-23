from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import DeleteDeviceView, DeviceDetailView, DeviceInventoryView, UpdateDeviceView,DeviceDashboardView,DeviceSearchView

urlpatterns = [
    path('', DeviceDashboardView.as_view(), name='device_dashboard'),
    path('inventory_view/', DeviceInventoryView.as_view(), name='inventory_view'),
    path('device/edit/<int:pk>/', UpdateDeviceView.as_view(), name='edit_device'),
    path('device/delete/<int:pk>/', DeleteDeviceView.as_view(), name='delete_device'),
    path('device/<int:pk>/<str:ip>/', DeviceDetailView.as_view(), name='device_detail'),
    path('device_search/', DeviceSearchView.as_view(), name='device_search'),
    
]