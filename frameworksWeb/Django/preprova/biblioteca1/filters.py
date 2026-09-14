import django_filters
from .models import Livro

class LivroFilter(django_filters.FilterSet):
    class Meta:
        model = Livro
        fields = ['autor', 'disponivel', 'ano_publicacao']