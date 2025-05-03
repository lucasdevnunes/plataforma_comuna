from django.db import models

class New(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo    
