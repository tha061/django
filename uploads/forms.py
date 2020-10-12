from django import forms
from . import models

class CreateLink(forms.ModelForm):
    class Meta:
        model = models.Link
        fields = ['link_text']

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
