from rest_framework.routers import DefaultRouter
from AppBom import viewsets

router = DefaultRouter()

router.register(prefix='state', viewset=viewsets.StateViewSet)

urlpatterns = router.urls