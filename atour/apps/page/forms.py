from socket import fromshare
from django import forms
from django.core.exceptions import ValidationError
from apps.page.models import Callback


class CallbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget = forms.Textarea(
            attrs={
                'rows': 5,
            }
        )
        
    class Meta:
        model = Callback
        fields = [
            'fio', 'phone', 'message',
        ]