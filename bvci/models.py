from django.db import models

# Create your models here.
class Actuligne(models.Model):
    nom = models.TextField()
    image = models.ImageField(upload_to='slide', default='1')
    image1 = models.ImageField(upload_to='slide',default='1')
    image2 = models.ImageField(upload_to='slide',default='1')
    imagecote = models.ImageField(upload_to='slide',default='1')
    description = models.TextField()

    def __str__(self):
        return self.nom



class Cour(models.Model):
    nomcour = models.CharField(max_length=200)
    doc = models.FileField()
    image_cour = models.ImageField()

    def __str__(self):
        return self.nomcour



class Matiere(models.Model):
    nommatiere = models.CharField( max_length=100, default=0)
    cour = models.ManyToManyField(Cour, related_name='cour')

    def __str__(self):
        return self.nommatiere

class Niveau(models.Model):
    nomniveau = models.CharField(max_length=90, default=0)
    matiere = models.ManyToManyField(Matiere, related_name='matieres')

    def __str__(self):
        return self.nomniveau



class Departement(models.Model):
    nomfaculte= models.CharField(max_length=500, default=0)
    descriptionfact = models.TextField()
    niveau = models.ManyToManyField(Niveau, related_name='niveaux')
    #slug=models.CharField(max_length=100 ,default=0 ,blank=True,null=True)
    
    def __str__(self):
        return self.nomfaculte


class Universite(models.Model):
    nom = models.CharField(max_length=100)

    @staticmethod
    def get_all_universites():
        return Universite.objects.all()

    def __str__(self):
        return self.nom
    
    
class Detail_Actualite(models.Model):
    video = models.FileField()
    titre = models.CharField(max_length=2000)

    @staticmethod
    def get_all_detail_Actualites():
        return Detail_Actualite.objects.all()

    def __str__(self):
        return self.titre

    
class Actualite(models.Model):
    nom_ecole = models.CharField(max_length=100)
    titre = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='actualite')
    descriprion = models.TextField()
    detail_Actualite = models.ForeignKey(Detail_Actualite, on_delete=models.CASCADE)
    universite = models.ForeignKey(Universite, on_delete=models.CASCADE)

    @staticmethod
    def get_all_actualites():
        return Actualite.objects.all()

    @staticmethod
    def get_all_actualites_by_actualiteid(universite_id):
        if universite_id:
            return Actualite.objects.filter(universite = universite_id)
        else:
            return Actualite.get_all_actualites()

    

class Ecole(models.Model):
    nom = models.CharField(max_length=200, default=0)
    logo= models.ImageField()
    description = models.TextField()
    departement = models.ManyToManyField(Departement, related_name='departements')
    slug=models.CharField(max_length=100, default=0)

    @staticmethod
    def get_all_ecoles():
        return Ecole.objects.all()

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('homeufhb',slug=[str(self.slug)])


class Contact(models.Model):
    nom_complet = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    numero = models.IntegerField()
    message = models.TextField()



    def __str__(self):
        return self.nom_complet
