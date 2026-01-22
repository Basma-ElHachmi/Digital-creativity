from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Project, AINavigator, Tag

# 1. Page d'accueil (Avec Algorithme de Recommandation)
def home(request):
    # Récupérer le profil de l'utilisateur depuis la "Session" (Mémoire temporaire)
    user_profile = request.session.get('user_profile')

    # Par défaut, on récupère TOUT
    courses = Course.objects.all()
    projects = Project.objects.all()

    # --- ALGORITHME DE FILTRAGE ---
    if user_profile:
        # On récupère les intérêts (IDs des tags) choisis par l'utilisateur
        interest_ids = user_profile.get('interests', [])
        
        if interest_ids:
            # On filtre : Garde seulement les cours/projets qui ont ces Tags
            # .distinct() évite les doublons
            courses = courses.filter(tags__id__in=interest_ids).distinct()
            projects = projects.filter(tags__id__in=interest_ids).distinct()

    # Les outils IA sont toujours affichés pour tout le monde
    ai_navigators = AINavigator.objects.all()

    context = {
        'courses': courses,
        'projects': projects,
        'ai_navigators': ai_navigators,
        'user_profile': user_profile, # Pour afficher "Bonjour Ahmed"
    }
    return render(request, 'index.html', context)

# 2. Page Profil (Formulaire)
def profile_view(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        # On sauvegarde les choix dans la session du navigateur
        request.session['user_profile'] = {
            'name': request.POST.get('name'),
            'level': request.POST.get('level'),
            'interests': request.POST.getlist('interests') # Liste des IDs cochés
        }
        return redirect('home') # Retour à l'accueil pour voir le résultat

    return render(request, 'profile.html', {'tags': tags})

# 3. Effacer le profil (Reset)
def clear_profile(request):
    if 'user_profile' in request.session:
        del request.session['user_profile']
    return redirect('home')

# 4. Détails d'un Cours
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

# 5. Détails d'un Projet
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})