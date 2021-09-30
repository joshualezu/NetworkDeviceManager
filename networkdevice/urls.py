from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import DeleteDeviceView, DeviceDetailView, DeviceInventoryView, UpdateDeviceView,DeviceDashboardView,DeviceSearchView,CreateDeviceView,DeviceConfigurationView,DeviceIssueView

urlpatterns = [
    path('', DeviceDashboardView.as_view(), name='device_dashboard'),
    path('inventory_view/', DeviceInventoryView.as_view(), name='inventory_view'),
    path('device/edit/<int:pk>/', UpdateDeviceView.as_view(), name='edit_device'),
    path('device/delete/<int:pk>/', DeleteDeviceView.as_view(), name='delete_device'),
    path('device/<int:pk>/<str:ip>/', DeviceDetailView.as_view(), name='device_detail'),
    path('device_search/', DeviceSearchView.as_view(), name='device_search'),
    path('create_device/', CreateDeviceView.as_view(), name='create_device'),
    path('device/config/<str:ip>/', DeviceConfigurationView.as_view(), name='device_configuration'),
    path('device/issue_list/', DeviceIssueView.as_view(), name='device_issues'),
]
