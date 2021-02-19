from django.shortcuts import render ,redirect

from django.contrib.auth.hashers import make_password, check_password
#from django.http import HttpResponse
from .models import *
from .forms import  ContactForm

from django.views import View
# Create your views here.
from .forms import CreateUserForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Votre compte a été créé '+ user)

            return redirect('loginPage')

    context={'form':form}
    return render(request,  'account/register.html', context) 

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            return redirect('index') 
        else:
            messages.info(request, 'Nom d utilisateur ou mot de pass incorrect')
    context={}
    return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage') 


@login_required(login_url='loginPage')
def index(request):
    ecoles = Ecole.objects.all();
    actulignes = Actuligne.objects.all();
    data  = {}
    data['ecoles'] = ecoles
    data['actulignes'] = actulignes
    return render(request, 'index.html' , data)


def utilisateur(request):
    ecoles = Ecole.objects.all()
    data  = {}
    data['ecoles'] = ecoles
    return render(request, 'account/utilisateur.html', data)



# Create your views here.

def contact(request):
    form = ContactForm()
    context={'form':form}
    message= ""
    error=""
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            message="Inscription validée ."
            return redirect('index')
        else:
            print(form.errors) 
            error="ok"
            form = FormulaireForm() 
    
    context={
        'form':form,
        'message':message,
        'error':error,
        }
    return render(request , 'blog/contact.html', context)



def boutique(request):
    return render(request, 'blog/boutique.html')


def actualite(request):
    actualites = None
    ecoles = Ecole.objects.all()
    universites = Universite.get_all_universites()
    universiteID = request.GET.get('universite')
    if universiteID:
        actualites = Actualite.objects.filter(universite=universiteID)
    else:
        actualites = Actualite.objects.all();
    data = {}
    data['ecoles'] = ecoles
    data['actualites'] = actualites
    data['universites'] = universites
    return render(request, 'blog/actualite.html', data)


def detailactualite(request , actualite_id):
    id= int(actualite_id)
    actualite = Actualite.objects.get(pk=actualite_id)
    
    context={
       'actualite':actualite,
        }
    return render(request, 'blog/detailactualite.html' , context)


def homeufhb(request , slug):
    #id= int(ecole_id)
    ecoles = Ecole.objects.all()
    ecole = Ecole.objects.get(slug=slug)
    departement=ecole.departement.all()
    
    context={
        'ecole':ecole,
        'departement':departement,
        }
    return render(request, 'homeufhb.html' , context)


def depart(request , departement_id):
    id = int(departement_id)
    departement = Departement.objects.get(id=departement_id)
    niveau=departement.niveau.all()

    context = {
       'departement':departement,
       'niveau' :niveau
    }
    return render(request, 'depart.html', context)


def lesmatieres(request , niveau_id):
    id = int(niveau_id)
    niveau = Niveau.objects.get(id=niveau_id)
    matiere=niveau.matiere.all()

    context = {
       'niveau' :niveau,
       'matiere' :matiere
    }
    return render(request, 'lesmatieres.html', context)



def cour(request, matiere_id):
    id = int(matiere_id)
    matiere = Matiere.objects.get(id=id)
    cour=matiere.cour.all()
    ecoles = Ecole.objects.all();
    if request.method =="POST":
        idcour = request.GET.get("document")
        for cou in cour:
            if cou.id == idcour:
                cou.inscriptions.add(request.inscription.id)
                print(cou.id)
            else:
                error = "erreur"
    context= {
        'ecoles':ecoles,
        'matiere' :matiere,
        'cour' :cour
    }
    return render(request, 'cour.html' , context)

 