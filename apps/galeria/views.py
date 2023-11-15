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

def editar_imagem(request, foto_id):
    fotografia = Cavaleiro.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        messages.success(request, 'Fotografia editada.')
        return redirect('apps.galeria:index')
    context = {
        'form': form,
        'foto_id': foto_id,
    }
    return render(request, 'galeria/editar_imagem.html', context)

def deletar_imagem(request, foto_id):
    fotografia = Cavaleiro.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia deletada.')
    return redirect('apps.galeria:index')

def filtro_imagem(request, armadura):
    cavaleiros = Cavaleiro.objects.order_by('armadura').filter(armadura=armadura)
    context = {
        'cavaleiros': cavaleiros
    }
    return render(request, 'galeria/index.html', context)