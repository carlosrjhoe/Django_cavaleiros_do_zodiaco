from django.shortcuts import redirect, render
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth

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
                return redirect('galeria:index')
                
            else:
                return redirect(template_name)
    
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
                return redirect(template_name)

            nome_casdatro = form['nome_casdatro'].value()
            email = form['email'].value()
            senha = form['primeira_senha'].value()

            if User.objects.filter(username=nome_casdatro).exists():
                return redirect(template_name)

            usuario = User.objects.create_user(
                username = nome_casdatro,
                email = email,
                password = senha,
            )
            usuario.save()
            return redirect('usuarios:login')
            
    context = {
        'form': form,
    }
    return render(request, template_name, context)