from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms as forms
from decouple import config


app_name = 'primary'

# Create your models here.


class ContactModelTwo(models.Model):
    Name = models.CharField(blank=False, max_length=30)
    Email = models.EmailField(blank=False)
    message = models.TextField(blank=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ContactModelTwo, self).__init__(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("primary:restaurants")
