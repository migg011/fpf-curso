from rest_framework import serializers
from .models import Autor, Livro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    autor_nome = serializers.CharField(source='autor.nome', read_only=True)

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'autor_nome', 'ano_publicacao', 'disponivel']