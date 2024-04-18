from django import forms
from .models import ContactForm


class ContactFormForm(forms.ModelForm):
  class Meta:
    model = ContactForm
    fields = ['customer_email','customer_name','message']



# class ContactFormForm(forms.Form):
#   custumer_email = forms.EmailField(label='correo')
#   custumer_name = forms.CharField(max_length=64, label='nombre')
#   message = forms.CharField(label='mensaje')