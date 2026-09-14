from rest_framework.routers import DefaultRouter
from .viewsets import AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = router.urls

