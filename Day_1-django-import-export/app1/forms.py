from django import forms

#Day 1
FORMAT_CHOICES = (
    ('csv','csv'),
    ('xls','xls'),
    ('json','json'),
)

class SelectFormatForm(forms.Form):
    """django form for selecting format of file."""
    format = forms.ChoiceField(choices=FORMAT_CHOICES)
    