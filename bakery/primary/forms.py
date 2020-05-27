from django import forms
from primary.models import ContactModelTwo
from django.core.files.images import get_image_dimensions
from django.core.mail import send_mail, BadHeaderError


class ContactFormTwo(forms.ModelForm):

    class Meta():
        model = ContactModelTwo
        fields = ('Name','Email','message',)

        widgets = {
            'Name':forms.TextInput(attrs={'class':'textinputclass'}),
            'message':forms.Textarea(attrs={'class':'message-container'}),
            'Email':forms.EmailInput()
        }
