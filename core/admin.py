from django.contrib import admin
from .models import Tag, UserProfile, Course, Resource, Project, AINavigator

# Permet d'ajouter des ressources directement dans la page du Cours (très pratique !)
class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [ResourceInline]
    list_display = ('title', 'level')
    search_fields = ('title',)

# Enregistrement des modèles
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(Course, CourseAdmin) # On utilise la version améliorée ici
admin.site.register(Resource)
admin.site.register(Project)
admin.site.register(AINavigator)
