from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cavaleiro(models.Model):

    OPCOES_CATEGORIAS = [
        ('BRONZE', 'Bronze'),
        ('OURO', 'Ouro'),
        ('PRATA', 'Prata'),
    ]
 
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user',
    )
    
    nome = models.CharField(max_length=100, blank=False, null=False)
    constelacao = models.CharField(max_length=100, blank=False, null=False)
    armadura = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default='')
    historia = models.TextField()
    imagem = models.ImageField(blank=True, upload_to='galeria/%Y%m')

    def __str__(self) -> str:
        return f'{self.nome} - {self.constelacao}'