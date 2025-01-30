# forms.py
from django import forms
from .models import Personne, Experience, Formation, Competence, Langue, Contact, Loisir, CV
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'date_naissance', 'photo']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['titre', 'entreprise', 'date_debut', 'date_fin', 'description']

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['diplome', 'institution', 'date_debut', 'date_fin', 'description']

class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = ['nom', 'niveau']

class LangueForm(forms.ModelForm):
    class Meta:
        model = Langue
        fields = ['langue', 'niveau']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'telephone', 'adresse']

class LoisirForm(forms.ModelForm):
    class Meta:
        model = Loisir
        fields = ['nom', 'description']

class CVForm(forms.ModelForm):
    DESIGN_CHOICES = [
        ('design1', 'Design 1'),
        ('design2', 'Design 2'),
        ('design3', 'Design 3'),
        ('design4', 'Design 4'),
    ]
    design = forms.ChoiceField(choices=DESIGN_CHOICES, required=True)
    experiences = forms.ModelMultipleChoiceField(
        queryset=Experience.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    competences = forms.ModelMultipleChoiceField(
        queryset=Competence.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    formations = forms.ModelMultipleChoiceField(
        queryset=Formation.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    langues = forms.ModelMultipleChoiceField(
        queryset=Langue.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    loisirs = forms.ModelMultipleChoiceField(
        queryset=Loisir.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = CV
        fields = ["personne", "contact", "experiences", "competences", "formations", "langues", "loisirs", "title", "design"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Récupérer l'utilisateur
        super().__init__(*args, **kwargs)
        if user:
            # Filtrer les choix pour les relations ManyToMany ou ForeignKey en fonction de l'utilisateur
            self.fields['personne'].queryset = Personne.objects.filter(user=user)
            self.fields['contact'].queryset = Contact.objects.filter(user=user)
            self.fields['experiences'].queryset = Experience.objects.filter(user=user)
            self.fields['formations'].queryset = Formation.objects.filter(user=user)
            self.fields['competences'].queryset = Competence.objects.filter(user=user)
            self.fields['langues'].queryset = Langue.objects.filter(user=user)
            self.fields['loisirs'].queryset = Loisir.objects.filter(user=user)
