from django.contrib import admin
from .models import Pregacao

@admin.register(Pregacao)
class PregacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    search_fields = ('titulo', 'descricao')
    list_filter = ('data_publicacao', 'autor')
    date_hierarchy = 'data_publicacao'
    ordering = ('-data_publicacao',)
