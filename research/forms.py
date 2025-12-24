from django import forms
from .models import ResearchDocument

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = ResearchDocument
        fields = ["file"]
