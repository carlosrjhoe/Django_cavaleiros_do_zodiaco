from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

# Create your views here.
def login(request):
    template_name = 'usuarios/login.html'
    form = LoginForms()
    context = {
        'form': form,
    }
    return render(request, template_name, context)

def cadastro(request):
    template_name = 'usuarios/cadastro.html'
    form = CadastroForms()
    context = {
        'form': form,
    }
    return render(request, template_name, context)