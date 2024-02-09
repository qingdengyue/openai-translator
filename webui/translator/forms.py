from django import forms
from .models import FileUpload

class FileTranslatorForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields=["title","cover"]