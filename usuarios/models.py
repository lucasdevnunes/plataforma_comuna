from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo email é obrigatório.')
        if not password:
            raise ValueError('A senha é obrigatória.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    def get_by_natural_key(self, email):
        return self.get(email=email)
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=150)
    funcao_na_igreja = models.CharField(max_length=150, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='usuarios/fotos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo']

    def __str__(self):
        return self.nome_completo
    