from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("livros/", include("livros.urls")),  # Inclui as rotas do app livros
]
