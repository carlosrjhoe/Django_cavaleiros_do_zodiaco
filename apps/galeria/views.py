from django.shortcuts import get_object_or_404, redirect, render
from apps.galeria.forms import FotografiaForms
from apps.galeria.models import Cavaleiro
from django.contrib import messages

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuário não logado!')
        return redirect('apps.usuarios:login')
    cavaleiro = Cavaleiro.objects.all()
    context = {
        'cavaleiros': cavaleiro
    }
    return render(request, 'galeria/index.html', context)

def imagem(request, foto_id):
    cavaleiro = get_object_or_404(Cavaleiro, pk=foto_id)
    context = {
        'cavaleiro': cavaleiro
    }
    return render(request, 'galeria/imagem.html', context)

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuário não logado!')
        return redirect('apps.usuarios:login')
    cavaleiro = Cavaleiro.objects.order_by('-nome')

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            cavaleiro = Cavaleiro.objects.filter(nome__icontains=nome_a_buscar)
        context = {
            'cavaleiros': cavaleiro
        }
    return render(request, 'galeria/buscar.html', context)

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuário não logado!')
        return redirect('apps.usuarios:login')
    
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada')
            return redirect('apps.galeria:index')
    context = {
        'form': form,
    }
    return render(request, 'galeria/nova_imagem.html', context)

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass