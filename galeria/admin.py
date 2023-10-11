from django.contrib import admin
from .models import Cavaleiro

# Register your models here.
class ListaCavaleiros(admin.ModelAdmin):
    list_display = ('id', 'nome', 'constelacao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )

admin.site.register(Cavaleiro, ListaCavaleiros)