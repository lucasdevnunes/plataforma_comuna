from django.contrib import admin
from .models import New

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('data_publicacao',)
    date_hierarchy = 'data_publicacao'
    ordering = ('-data_publicacao',)
