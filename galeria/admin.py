from django.contrib import admin
from .models import Cavaleiro

# Register your models here.
class ListaCavaleiros(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'nome', 'armadura', 'constelacao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_filter = ('armadura', 'usuario')

admin.site.register(Cavaleiro, ListaCavaleiros)