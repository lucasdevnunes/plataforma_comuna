from django.db import models
from django.core.exceptions import ValidationError

class New(models.Model):
    titulo = models.CharField(max_length=200, db_index=True)
    resumo = models.TextField()
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.titulo    

    def clean(self):
        if not self.conteudo:
            raise ValidationError('O conteúdo do artigo não pode estar vazio.')        