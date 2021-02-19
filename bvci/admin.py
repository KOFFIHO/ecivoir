from django.contrib import admin

# Register your models here.

from .models import *

class AdminDetail_Actualite(admin.ModelAdmin):
    list_display = ['titre']

class AdminActualite(admin.ModelAdmin):
    list_display = ['titre', 'universite' , 'detail_Actualite']

class AdminContact(admin.ModelAdmin):
    list_display = ['nom_complet', 'email' , 'numero' , 'message']

# Register your models here.

admin.site.register(Ecole)
admin.site.register(Departement)
admin.site.register(Matiere)
admin.site.register(Cour)
admin.site.register(Niveau)
admin.site.register(Detail_Actualite, AdminDetail_Actualite)
admin.site.register(Actualite, AdminActualite)
admin.site.register(Universite)
admin.site.register(Contact, AdminContact)

admin.site.register(Actuligne)
