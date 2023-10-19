from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class LoginTemplateView(TemplateView):
    template_name = 'usuarios/login.html'

class CadastroTemplateView(TemplateView):
    template_name = 'usuarios/cadastro.html'