from django.contrib import admin
from django.urls import path, include # <--- N'oublie pas d'importer include !

urlpatterns = [
    # La route vers l'interface admin (déjà là par défaut)
    path('admin/', admin.site.urls),
    
    # La route vers ton application. 
    # Ça veut dire : "Tout ce qui arrive à la racine du site, envoie-le vers core.urls"
    path('', include('core.urls')), 
]