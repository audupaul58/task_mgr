from django.forms import ModelForm
from .models import Contact, AirdropModel


class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'

class AirdropForm(ModelForm):
    
    class Meta:
        model = AirdropModel
        fields = ('url', 'title',  'frequency', 'network', 'wallet', 'completed', 'endDate', 'walletCode')