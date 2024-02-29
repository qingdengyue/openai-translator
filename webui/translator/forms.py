from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import BaseFormSet, TextInput, formset_factory

from django_bootstrap5.widgets import RadioSelectButtonGroup

from .models import FileUpload


SUPPORT_LANGUAGE = (
    ("1", "简体中文"),
    ("2", "繁体中文"),
    ("3", "English"),
    ("4", "日本語"),
)
SUPPORT_LANGUAGE_DEFAULT = "1"


def getLanguage(code):
    for lang_code, lang_name in SUPPORT_LANGUAGE:
        if lang_code == code:
            return lang_name
    return "简体中文"


SUPPORT_FORMAT = (
    ("1", "PDF"),
    ("2", "Markdown"),
)


SUPPORT_FORMAT_DEFAULT = "1"


def getFormat(format):
    for format_code, format_name in SUPPORT_FORMAT:
        if format_code == format:
            return format_name
    return "pdf"


class FilesForm(forms.Form):
    pdfUpload = forms.FileField(
        widget=forms.ClearableFileInput, label="Please upload file(pdf):", required=True)
    fileLanguageList = forms.ChoiceField(
        choices=SUPPORT_LANGUAGE, label="Target Language:", required=True, initial=SUPPORT_LANGUAGE_DEFAULT)
    fileFormatList = forms.ChoiceField(
        choices=SUPPORT_FORMAT, label="Traget Format:", required=True, initial=SUPPORT_FORMAT_DEFAULT)
    use_required_attribute = True

