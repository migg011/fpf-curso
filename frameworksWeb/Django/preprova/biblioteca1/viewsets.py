from rest_framework import viewsets
from .models import Autor, Livro
from .serializers import AutorSerializer, LivroSerializer
from .filters import LivroFilter

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter