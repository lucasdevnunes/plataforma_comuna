from django.contrib import admin
from .models import Artigo

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('data_publicacao', 'autor')
    date_hierarchy = 'data_publicacao'
    ordering = ('-data_publicacao',)