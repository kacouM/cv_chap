from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.trombinoscope, name='trombinoscope'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('EtatCivil/', views.etat_civil, name='EtatCivil'),
    path('TdeBord/', views.TdeBord, name='TdeBord'),
    path('experiencePro/', views.experience_pro, name='experiencePro'),
    path('formation/', views.addFormaton, name='formation'),
    path('competence/', views.addCompetence, name='competence'),
    path('langue/', views.addLangue, name='langue'),
    path('loisir/', views.addLoisir, name='loisir'),
    path('creerLe_cv/', views.CreationCV, name='creerLe_cv'),
    path('contact__/', views.contact__, name='contact__'),
    path('aff_CV/<int:cv_id>/', views.aff_CV, name='aff_CV'),
    
    # Ajoutez une route par défaut pour la page de formulaire d'authentification
    path('connexion', views.formulaire, name='formulaire'),
    
    # Réécrivez les routes pour créer ou éditer les autres tables
    path('etat_civil/', views.etat_civil, name='etat_civil'),
    path('TdeBord/', views.TdeBord, name='TdeBord'),
    path('experience_pro/', views.experience_pro, name='experience_pro'),
    path('addFormaton/', views.addFormaton, name='addFormaton'),
    path('addCompetence/', views.addCompetence, name='addCompetence'),
    path('addLangue/', views.addLangue, name='addLangue'),
    path('addLoisir/', views.addLoisir, name='addLoisir'),
    path('CreationCV/', views.CreationCV, name='CreationCV'), 
    path('register/', views.register, name='register'),
    path('contact__/', views.contact__, name='contact__'),






    path('aff_experiences/', views.aff_experiences, name='aff_experiences'),
    path('aff_formations/', views.aff_formations, name='aff_formations'),
    path('aff_competences/', views.aff_competences, name='aff_competences'),
    path('aff_langue/', views.aff_langue, name='aff_langue'),
    path('aff_loisirs/', views.aff_loisirs, name='aff_loisirs'),
     # Personne
    path('aff_personne/', views.aff_personne, name='aff_personne'),
    # Contact
    path('aff_contact/', views.aff_contact, name='aff_contact'),
    # CVs
    path('list_cv/', views.list_cv, name='list_cv'),

    path('trombinoscope/', views.trombinoscope, name='trombinoscope'),
    path('cv/<int:pk>/', views.cv_detail, name='cv_detail'),  # Vue pour afficher le CV
   # pour rediriger vers la vue qui permet de modifier
    path('cv/<int:cv_id>/edit/', views.edit_cv, name='edit_cv'),
# pour rediriger vers la vue qui permet de surprimer
    path('cv/<int:cv_id>/delete/', views.supretionCV, name='supretionCV'),
#liens pour envoyer par mail
path("cv/<int:cv_id>/send_email/", views.CV_Pemail, name="CV_Pemail"),
]
