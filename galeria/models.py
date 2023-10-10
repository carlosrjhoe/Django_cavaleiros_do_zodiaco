from django.db import models

# Create your models here.
class Cavaleiro(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    constelacao = models.CharField(max_length=100, blank=False, null=False)
    historia = models.TextField()
    imagem = models.ImageField(upload_to='assets/imagens/galeria/%Y%m',blank=True)

    def __str__(self) -> str:
        return f'{self.nome} - {self.constelacao}'

    objects = models.Manager()