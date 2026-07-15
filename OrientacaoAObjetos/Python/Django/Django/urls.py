from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sale/', include('AppBom.urls'), name='api-root'),
]