from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from appRestaurante import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('admin/', admin.site.urls),
    # Login - Cada vez que un usuario se logue se les genera un token de refresh(24 horas) y un primer token de acceso(5 minutos) 
    path('login/',         TokenObtainPairView.as_view()), 
    # refresh - Se recibe como parametro un token de refresh para generar un nuevo token de acceso
    path('refresh/',       TokenRefreshView.as_view()),
    path('user/',          views.UserCreateView.as_view()), # vista creada en el proyecto para la creacion de un usuario
    path('user/<int:pk>/', views.UserDetailView.as_view()), # vista creada en el proyecto para consultar un usuario
    path('verifyToken/', views.VerifyTokenView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
