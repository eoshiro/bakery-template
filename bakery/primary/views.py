from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import ContactFormTwo
from .models import ContactModelTwo
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from portfoliosite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, BadHeaderError
from . import forms
from portfoliosite import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from decouple import config


# RestaurantViews

class RestaurantView(TemplateView):
    template_name = 'restaurant/restaurant-contact.html'

class RestaurantBaseView(TemplateView):
    template_name = 'restaurant/restaurant-base.html'


class RestaurantContactView(CreateView):
    template_name = 'restaurant/restaurant-contact.html'
    form_class = ContactFormTwo
    model = ContactModelTwo
    redirect_field_name = 'restaurant/restaurant-contact.html'
    def form_valid( self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('Name'),
            email=form.cleaned_data.get('Email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))

        send_mail(
            subject='A Message from Oshiro-Codes',
            message=message,
            from_email='email',
            recipient_list=[config('EMAIL_HOST_USER')],
            fail_silently = False
            )
        def mailsent(request):
            return render(request, 'restaurant/restaurant-contact.html')
        return super(ContactFormView, self).form_valid(form)
