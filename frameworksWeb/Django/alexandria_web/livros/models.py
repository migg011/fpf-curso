from django.db import models


class Livro(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.titulo} ({self.codigo})"
