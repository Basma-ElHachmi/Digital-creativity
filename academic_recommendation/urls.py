from django.contrib import admin
from django.urls import path, include # Importe bien 'include'
from django.contrib.auth import views as auth_views
from core import views # Assure-toi que ton dossier s'appelle 'core'

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- 1. AUTHENTIFICATION ---
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),

    # --- 2. TON APPLICATION (HOME, PROFILE, ETC.) ---
    # Cette ligne est celle qui manque pour enlever l'erreur 404 !
    path('', include('core.urls')), 
]