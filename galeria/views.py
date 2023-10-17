from django.shortcuts import get_object_or_404, render
from .models import Cavaleiro

# Create your views here.
def index(request):
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