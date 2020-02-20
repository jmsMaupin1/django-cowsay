from django import forms

from cow_say.models import CowText

class CowEchoForm(forms.ModelForm):
    class Meta:
        model = CowText
        fields = [
            'text',
            'template'
        ]
        widgets = {
            'text': forms.TextInput(attrs={'class': 'cow-input'}),
        }