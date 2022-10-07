from socket import fromshare
from django import forms
from django.core.exceptions import ValidationError
from apps.feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    """Форма отзывов"""           
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fio'].widget = forms.TextInput(
            attrs={
                'placeholder':self.fields['fio'].label,
            }
        )
        self.fields['body'].widget = forms.Textarea(
            attrs={
                'rows':5,
                'placeholder':self.fields['body'].label,
            }
        )
        
    class Meta:
        model = Feedback
        fields = [
            'fio', 'rating', 'body',
        ]
    