from django import forms
from .models import Code

class CodeForm(forms.ModelForm):
    """"""
    number = forms.CharField(label='Code')
    class Meta:
        model = Code
        fields = ('number',)