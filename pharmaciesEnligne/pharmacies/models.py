from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here



class Categorie(models.Model):
     nom = models.CharField(max_length=255)
    
     def __str__(self):
        return self.nom



class Client(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()

    def __str__(self):
        return self.nom
   

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.Medicament} - {self.client} - {self.date}"

class Pharmacien(User):
     nom = models.CharField(max_length=255)
     telephone = models.CharField(max_length=20)
     adresse = models.TextField()
     def __str__(self):
        return self.nom


class Pharmacie(models.Model):
    Pharmacien = models.ForeignKey(Pharmacien, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    def __str__(self):
        return self.nom
    
    
class Medicament(models.Model):
    pharmacie = models.ForeignKey(Pharmacie, on_delete=models.CASCADE)
    catagorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE,  null=True, blank=True)
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()
    disponible = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='img', blank=True)

    def __str__(self):
        return self.nom