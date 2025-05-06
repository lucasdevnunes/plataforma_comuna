from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'nome_completo', 'funcao_na_igreja', 'is_active', 'last_login')
    list_filter = ('is_staff', 'funcao_na_igreja')
    search_fields = ('email', 'nome_completo')
    ordering = ('email',)

    readonly_fields = ('last_login', 'date_joined')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('nome_completo', 'funcao_na_igreja', 'foto_perfil')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome_completo', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('email',)
        return self.readonly_fields