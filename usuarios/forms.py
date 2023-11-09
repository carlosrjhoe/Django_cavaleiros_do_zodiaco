from typing import Any
from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(label='Nome de login', required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ex.: João Silva',
        }
    ))
    
    senha = forms.CharField(label='Senha', required=True, max_length=50, widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
        }
    ))

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label='Nome de cadastro', required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ex.: João Silva',
        }
    ))

    email = forms.EmailField(label='Email', required=True, max_length=50, widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ex.: nome@email.com',
        }
    ))

    primeira_senha = forms.CharField(label='Senha', required=True, max_length=50, widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
        }
    ))

    segunda_senha = forms.CharField(label='Confirme sua Senha', required=True, max_length=50, widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Digite sua senha novamente',
        }
    ))

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não é possível incerir espaços dentro do compo (nome cadastro).')
            else:
                return nome

    def clean_segunda_senha(self):
        primeira_senha = self.cleaned_data.get('primeira_senha')
        segunda_senha = self.cleaned_data.get('segunda_senha')
        if primeira_senha and segunda_senha:
            if primeira_senha != segunda_senha:
                raise forms.ValidationError('As senhas não são iguais.')
            else:
                return segunda_senha