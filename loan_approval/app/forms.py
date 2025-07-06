from django import forms
from .models import ApprovalModel


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = ApprovalModel
        fields = '__all__'