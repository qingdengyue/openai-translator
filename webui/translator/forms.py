from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import BaseFormSet, TextInput, formset_factory

from django_bootstrap5.widgets import RadioSelectButtonGroup

from .models import FileUpload


RADIO_CHOICES = (("1", "Radio 1"), ("2", "Radio 2"))

MEDIA_CHOICES = (
    ("Audio", (("vinyl", "Vinyl"), ("cd", "CD"))),
    ("Video", (("vhs", "VHS Tape"), ("dvd", "DVD"))),
    ("unknown", "Unknown"),
)



class FileTranslatorForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields=["title","cover"]


class FilesForm(forms.Form):
    pdfUpload = forms.FileField(widget=forms.ClearableFileInput,label="Please upload file(pdf):")

    use_required_attribute = False
