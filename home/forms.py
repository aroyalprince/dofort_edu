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
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Enter your message here...',
                'rows': 4
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].label = ''