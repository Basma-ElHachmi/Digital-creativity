from django.shortcuts import render
# IMPORTANT : On importe les modèles que TU as créés dans models.py
# Si ces noms n'étaient pas identiques à ceux de models.py, ça ne marcherait pas.
from .models import Course, Project, AINavigator, UserProfile, Tag, Resource

def home(request):
    
    # Il demande à la base de données de lui donner tous les objets
    courses = Course.objects.all()       
    projects = Project.objects.all()     
    ai_navigators = AINavigator.objects.all() 

    
    # On met les données dans un dictionnaire pour les envoyer au HTML
    context = {
        'courses': courses,
        'projects': projects,
        'ai_navigators': ai_navigators,
    }
    
    
    return render(request, 'index.html', context)
