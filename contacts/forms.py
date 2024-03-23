from django import forms
from .models import Contacts


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['contact_id','contact_name','contact_email','contact_address','contact_phone']