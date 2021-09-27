from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import PasswordChangingForm, AccountChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.db import models

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

class PasswordsChangeView(LoginRequiredMixin, PasswordChangeView):
    login_url= 'login'
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'

class AccountEditView(LoginRequiredMixin, generic.UpdateView):
    login_url = 'login'
    form_class = AccountChangeForm
    template_name = 'registration/edit_account.html'
    success_url = reverse_lazy('device_dashboard')

    def get_object(self):
        return self.request.user
