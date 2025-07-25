from django import forms
from .models import Admission, Enquiry, ContactMessage



class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'
 