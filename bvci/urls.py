from django.urls import path
from django.conf.urls import url
from .views import index, homeufhb , depart , lesmatieres, cour, actualite, boutique, contact, detailactualite # , Nouveauapprenant
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', index , name='index'),

    path('account/register/', views.register, name='registerPage'),
    path('account/utilisateur/', views.utilisateur, name='utilisateur'),
    path('account/login/', views.loginPage, name='loginPage'),
    path('account/logout/', views.logoutUser, name='logout'),

    path('actualite',actualite , name='actualite'),
    path('boutique',boutique , name='boutique'),
    path('contact',contact , name='contact'),
    path('ecoles/<slug>/', homeufhb, name='homeufhb'),
    url(r'^departement/(?P<departement_id>[0-9]+)$', depart, name='depart'),
    url(r'^niveau/(?P<niveau_id>[0-9]+)$', lesmatieres, name='lesmatieres'),
    url(r'^cour/(?P<matiere_id>[0-9]+)$', cour, name='cour'),
    url(r'^actualites/(?P<actualite_id>[0-9]+)$', detailactualite, name='detailactualite'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)