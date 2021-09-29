from django.views.generic import UpdateView, DeleteView, ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from .models import NetworkDevice
from .forms import EditDeviceForm, CreateDeviceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.postgres.search import SearchVector

app_name = 'networkdevice'

# View for device dashboard
# Main view
class DeviceDashboardView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'networkdevice/device_dashboard.html'
    model = NetworkDevice
    ordering=['pingable', '-last_ping']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['offline'] = NetworkDevice.objects.all().filter(pingable=False)
        return data

# View displays device serial numbers in table
class DeviceInventoryView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'networkdevice/inventory_view.html'
    model = NetworkDevice
    ordering = ['ip']

    # IF query passed, return results
    # Otherwise, show all objects
    def get_queryset(self):
        object_list = NetworkDevice.objects.all()
        query = self.request.GET.get('inventorysearch', '')
        if query:
            object_list = NetworkDevice.objects.annotate(search=SearchVector(
                'ip',
                'hostname',
                'serial_1',
                'serial_2',
                'serial_3',
                'serial_4',
                'serial_5',
                'serial_6',
                'serial_7',
                'serial_8',
                'serial_9',
                'pingable'
            ),).filter(search__icontains=query)
        return object_list

# Provides view for navbar search
class DeviceSearchView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'networkdevice/device_search.html'
    model = NetworkDevice

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['query'] = self.request.GET.get('name', '')
        return data

    def get_queryset(self):
        object_list = ''
        query = self.request.GET.get('name', '')
        if query:
            object_list = NetworkDevice.objects.annotate(search=SearchVector(
                'ip',
                'hostname',
                'serial_1',
                'serial_2',
                'serial_3',
                'serial_4',
                'serial_5',
                'serial_6',
                'serial_7',
                'serial_8',
                'serial_9',
                'pingable'
            ),).filter(search__icontains=query)
        return object_list

# View for specfic device
class DeviceDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    def get(self,request,*args,**kwargs):
        device = get_object_or_404(NetworkDevice, ip = kwargs['ip'], id = kwargs['pk'])
        context = {'device':device}
        return render(request, 'networkdevice/detail.html', context)

# View to update device information
class UpdateDeviceView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = NetworkDevice
    form_class = EditDeviceForm
    template_name = 'networkdevice/edit_device.html'

# Confirm deletion of device
class DeleteDeviceView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = NetworkDevice
    template_name = 'networkdevice/delete_device.html'
    success_url = reverse_lazy('device_dashboard')

class CreateDeviceView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = NetworkDevice
    form_class = CreateDeviceForm
    template_name = 'networkdevice/create_device.html'

class DeviceConfigurationView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    def get(self,request,*args,**kwargs):
        device = get_object_or_404(NetworkDevice, ip = kwargs['ip'])
        context = {'device':device}
        return render(request, 'networkdevice/configuration.html', context)
