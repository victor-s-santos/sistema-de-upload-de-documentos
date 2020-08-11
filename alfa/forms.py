from django.utils import timezone
from django import forms
from .models import Documentos

class DocumentosForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['nome','documento']