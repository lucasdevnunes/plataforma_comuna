from django.db import models

class Artigos(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
