from django import forms
from .models import NetworkDevice

class EditDeviceForm(forms.ModelForm):

    ip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IP'}), label='')
    hostname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hostname'}), label='')
    device_model = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model'}), label='')
    note = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note'}), label='')
    serial_1 = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'11', 'class': 'form-control', 'placeholder': 'Serial 1'}), label='')
    serial_2 = forms.CharField(required = False, widget=forms.TextInput(attrs={'maxlength':'11', 'class': 'form-control', 'placeholder': 'Serial 2'}), label='')
    serial_3 = forms.CharField(required = False, widget=forms.TextInput(attrs={'maxlength':'11', 'class': 'form-control', 'placeholder': 'Serial 3'}), label='')
    serial_4 = forms.CharField(required = False, widget=forms.TextInput(attrs={'maxlength':'11', 'class': 'form-control', 'placeholder': 'Serial 4'}), label='')
    serial_5 = forms.CharField(required = False, widget=forms.TextInput(attrs={'maxlength':'11', 'class': 'form-control', 'placeholder': 'Serial 5'}), label='')
    serial_6 = forms.CharField(required = False, widget=forms.TextInput(attrs={'maxlength':'11', 'class': 'form-control', 'placeholder': 'Serial 6'}), label='')
    serial_7 = forms.CharField(required = False, widget=forms.TextInput(attrs={'maxlength':'11', 'class': 'form-control', 'placeholder': 'Serial 7'}), label='')
    serial_8 = forms.CharField(required = False, widget=forms.TextInput(attrs={'maxlength':'11', 'class': 'form-control', 'placeholder': 'Serial 8'}), label='')
    serial_9 = forms.CharField(required = False, widget=forms.TextInput(attrs={'maxlength':'11', 'class': 'form-control', 'placeholder': 'Serial 9'}), label='')

    class Meta:
        model = NetworkDevice
        fields = ('ip', 'hostname', 'device_model', 'note', 'serial_1', 'serial_2', 'serial_3', 'serial_4', 'serial_5', 'serial_6', 'serial_7', 'serial_8', 'serial_9')