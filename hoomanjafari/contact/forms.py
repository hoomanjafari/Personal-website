from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '... موضوع'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '... ایمیل'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '... شماره تماس' }),
            'body': forms.Textarea(attrs={'class': 'form-control', 'style': 'resize:none;', 'placeholder': ' ... پیام خود را بنویسید'}),
        }
        labels = {
            'subject': '',
            'email': '',
            'number': '',
            'body': ''
        }
