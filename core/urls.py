from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    
   
    path('profile/', views.profile_view, name='profile'),
    path('clear-profile/', views.clear_profile, name='clear_profile'),

    
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]