from socket import fromshare
from django import forms
from django.core.exceptions import ValidationError
from apps.tour.models import Order


class OrderForm(forms.ModelForm):
    """Форма заказа тура"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fio'].widget = forms.TextInput(
            attrs={
                'placeholder':self.fields['fio'].label,
            }
        )
        self.fields['phone'].widget = forms.TextInput(
            attrs={
                'placeholder':self.fields['phone'].label,
            }
        )  
        self.fields['email'].widget = forms.TextInput(
            attrs={
                'placeholder':self.fields['email'].label,
            }
        )               
        self.fields['message'].widget = forms.Textarea(
            attrs={
                'rows':5,
                'placeholder':self.fields['message'].label,
            }
        )
        
    class Meta:
        model = Order
        fields = [
            'fio', 'phone', 'email', 'message',
        ]
