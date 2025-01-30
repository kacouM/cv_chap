from django.db import models
from django.contrib.auth.models import User

class Personne(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    #photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, default='photos/default-photo.jpg')
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.titre} chez {self.entreprise}"

class Formation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diplome = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.diplome} à {self.institution}"

class Competence(models.Model):
    NIVEAU_CHOICES = [
        ('Débutant', 'Débutant'),
        ('Intermédiaire', 'Intermédiaire'),
        ('Avancé', 'Avancé'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} - {self.niveau}"

class Langue(models.Model):
    NIVEAU_CHOICES = [
        ('Débutant', 'Débutant'),
        ('Intermédiaire', 'Intermédiaire'),
        ('Avancé', 'Avancé'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    langue = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.langue} - {self.niveau}"

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email

class Loisir(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom

class CV(models.Model):
    DESIGN_CHOICES = [
        ('design1', 'Design 1'),
        ('design2', 'Design 2'),
        ('design3', 'Design 3'),
        ('design4', 'Design 4'),
    ]
    design = models.CharField(max_length=10, choices=DESIGN_CHOICES, default='design1')
    title = models.CharField(max_length=100,default='CV sans titre')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)  # Modifié de OneToOneField à ForeignKey
    experiences = models.ManyToManyField(Experience, blank=True)
    formations = models.ManyToManyField(Formation, blank=True)
    competences = models.ManyToManyField(Competence, blank=True)
    langues = models.ManyToManyField(Langue, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)  # Modifié de OneToOneField à ForeignKey
    loisirs = models.ManyToManyField(Loisir, blank=True)

    def __str__(self):
        return f"CV de {self.personne.prenom} {self.personne.nom}"
