from django.db import models

# Pour les tags (ex: Python, Web, IA)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

# Pour le profil étudiant (Niveau + Intérêts)
class UserProfile(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Débutant'),
        ('intermediate', 'Intermédiaire'),
        ('advanced', 'Avancé'),
    ]
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    interests = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.name

# Carte 1 : Les COURS
class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Débutant'),
        ('intermediate', 'Intermédiaire'),
        ('advanced', 'Avancé'),
    ]
    title = models.CharField(max_length=150)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.title

# Les RESSOURCES DANS LES COURS (C'est ici que tu mettras les liens)
class Resource(models.Model):
    RESOURCE_TYPE = (
        ('video', 'Vidéo'),
        ('pdf', 'PDF'),
        ('site', 'Site Web'),
    )
    title = models.CharField(max_length=150)
    link = models.URLField()
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPE)
    # Le lien magique vers le cours
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='resources')

    def __str__(self):
        return self.title

# Carte 2 : Les PROJETS
class Project(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Débutant'),
        ('intermediate', 'Intermédiaire'),
        ('advanced', 'Avancé'),
    ]
    title = models.CharField(max_length=150)
    description = models.TextField() 
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    tags = models.ManyToManyField(Tag, blank=True)
    # AJOUT : Le lien pour faire fonctionner le bouton "Lancer le projet"
    project_url = models.URLField(max_length=500, blank=True, null=True) 

    def __str__(self):
        return self.title

# Carte 3 : IA NAVIGATOR (Juste les sites utiles)
class AINavigator(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField() # Le lien vers l'outil IA
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.name