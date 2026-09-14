from django.shortcuts import render
from .models import Livro


def listar_livros(request):
    # Busca todos os livros cadastrados no banco de dados
    livros = Livro.objects.all()

    # Passa a lista para o template HTML renderizar
    return render(request, "livros/listar.html", {"livros": livros})
