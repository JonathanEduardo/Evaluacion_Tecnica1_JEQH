from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestion.views import AutorViewSet, LibroViewSet


# Enrutador (router)
router = DefaultRouter()

# ViewSets  automatic endpoints creation
router.register(r'autores', AutorViewSet) # /api/autores
router.register(r'libros', LibroViewSet)  # /api/libros


# Include 'api' for endpoint access
urlpatterns = [
     path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]