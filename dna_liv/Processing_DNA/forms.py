from django import forms

class DNASequenceForm(forms.Form):
    sequence = forms.CharField(
        label='Последовательность ДНК',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Последовательность ДНК',
        })
    )