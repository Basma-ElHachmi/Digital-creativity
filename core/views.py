from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required # <--- AJOUTÉ
from .models import Course, Project, AINavigator, Tag

# 1. Page d'accueil (Accès restreint aux connectés)
@login_required # <--- AJOUTÉ : Protection
def home(request):
    # Récupérer le profil de l'utilisateur depuis la Session
    user_profile = request.session.get('user_profile')

    courses = Course.objects.all()
    projects = Project.objects.all()

    # --- ALGORITHME DE FILTRAGE ---
    if user_profile:
        interest_ids = user_profile.get('interests', [])
        if interest_ids:
            courses = courses.filter(tags__id__in=interest_ids).distinct()
            projects = projects.filter(tags__id__in=interest_ids).distinct()

    ai_navigators = AINavigator.objects.all()

    context = {
        'courses': courses,
        'projects': projects,
        'ai_navigators': ai_navigators,
        'user_profile': user_profile, 
    }
    # Attention : vérifie si ton fichier s'appelle index.html ou home.html
    return render(request, 'index.html', context)

# 2. Page Profil
@login_required # <--- AJOUTÉ
def profile_view(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        request.session['user_profile'] = {
            'name': request.POST.get('name'),
            'level': request.POST.get('level'),
            'interests': request.POST.getlist('interests')
        }
        return redirect('home')

    return render(request, 'profile.html', {'tags': tags})

# 3. Effacer le profil (Reset)
@login_required # <--- AJOUTÉ
def clear_profile(request):
    if 'user_profile' in request.session:
        del request.session['user_profile']
    return redirect('home')

# 4. Détails d'un Cours
@login_required # <--- AJOUTÉ
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

# 5. Détails d'un Projet
@login_required # <--- AJOUTÉ
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Connecte l'utilisateur direct après inscription
            return redirect('profile') # Envoie-le configurer son profil
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})