from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # --- AUTHENTIFICATION ---
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'), # AJOUTÉ ICI

    # --- PAGES DU DASHBOARD ---
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('clear-profile/', views.clear_profile, name='clear_profile'),

    # --- DÉTAILS ---
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]