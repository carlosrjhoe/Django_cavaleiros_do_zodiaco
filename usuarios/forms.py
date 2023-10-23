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
    nome_casdatro = forms.CharField(label='Nome de cadastro', required=True, max_length=100, widget=forms.TextInput(
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