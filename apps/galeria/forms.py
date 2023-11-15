from django import forms
from apps.galeria.models import Cavaleiro

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Cavaleiro
        exclude = ['usuario',]
        labels = {
            'constelacao': 'Constelação',
            'historia': 'História',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'constelacao': forms.TextInput(attrs={'class': 'form-control'}),
            'armadura': forms.Select(attrs={'class': 'form-control'}),
            'historia': forms.Textarea(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
        }