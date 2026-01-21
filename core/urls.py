from django.urls import path
from . import views # On importe tes vues (le "Chef Cuisinier")

urlpatterns = [
    # Si l'URL est vide (''), on appelle la fonction 'home' dans views.py
    path('', views.home, name='home'),
]