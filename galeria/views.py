from django.shortcuts import render
from .models import Cavaleiro

# Create your views here.
def index(request):
    cavaleiro = Cavaleiro.objects.all()
    context = {
        'cavaleiros': cavaleiro
    }
    return render(request, 'galeria/index.html', context)

def imagem(request):
    return render(request, 'galeria/imagem.html')