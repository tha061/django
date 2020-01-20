from django import forms
from . import models

class CreateLink(forms.ModelForm):
    class Meta:
        model = models.Link
        fields = ['link_text']
