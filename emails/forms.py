from django import forms

from .models import EmailEntry

class EmailEntryForm(forms.ModelForm):
    class Meta:
        model=EmailEntry
        fields= ['email']