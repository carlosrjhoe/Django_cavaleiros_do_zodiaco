from django.shortcuts import redirect, render
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

    if request == 'POST':
        form = CadastroForms(request.POST)
        if form['primeira_senha'].value() != form['segunda_senha'].value():
            return redirect(template_name)
        
    context = {
        'form': form,
    }
    return render(request, template_name, context)