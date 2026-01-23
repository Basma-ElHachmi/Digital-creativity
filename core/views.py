from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q # Importé pour une recherche plus puissante
from .models import Course, Project, AINavigator, Tag

# 1. Page d'accueil (Avec Algorithme de Recommandation + Recherche)
@login_required
def home(request):
    user_profile = request.session.get('user_profile')
    
    # Récupérer le paramètre de recherche 'q' depuis l'URL
    query = request.GET.get('q')

    courses = Course.objects.all()
    projects = Project.objects.all()

    # --- LOGIQUE DE RECHERCHE ---
    if query:
        # Cherche dans le titre OU la description
        courses = courses.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).distinct()
        projects = projects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).distinct()
    
    # --- ALGORITHME DE FILTRAGE (Seulement si aucune recherche n'est active) ---
    elif user_profile:
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
        'query': query, # On renvoie la requête pour l'afficher dans l'input
    }
    return render(request, 'index.html', context)

# 2. Inscription (Register)
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# 3. Page Profil (Formulaire d'intérêts)
@login_required
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

# 4. Effacer le profil (Reset)
@login_required
def clear_profile(request):
    if 'user_profile' in request.session:
        del request.session['user_profile']
    return redirect('home')

# 5. Détails d'un Cours
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

# 6. Détails d'un Projet
@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})