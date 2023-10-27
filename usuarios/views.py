from django.shortcuts import redirect, render
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    template_name = 'usuarios/login.html'
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                username = nome,
                password = senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'Usuário {nome} logado com sucesso')
                return redirect('galeria:index')
                
            else:
                messages.error(request, f'Erro ao efetua login.')
                return redirect('galeria:index')
    
    context = {
        'form': form,
    }
    return render(request, template_name, context)

def cadastro(request):
    template_name = 'usuarios/cadastro.html'
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form['primeira_senha'].value() != form['segunda_senha'].value():
                messages.error(request, 'Senhas não são iguais')
                return redirect(template_name)

            nome_casdatro = form['nome_casdatro'].value()
            email = form['email'].value()
            senha = form['primeira_senha'].value()

            if User.objects.filter(username=nome_casdatro).exists():
                messages.error(request, 'Usuário já existente.')
                return redirect(template_name)

            usuario = User.objects.create_user(
                username = nome_casdatro,
                email = email,
                password = senha,
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso.')
            return redirect('usuarios:login')
            
    context = {
        'form': form,
    }
    return render(request, template_name, context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout do usuário efetuado com sucesso.')
    return redirect('usuarios:login')