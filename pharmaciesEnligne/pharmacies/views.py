from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework import generics ,viewsets

from .models import Medicament, Categorie, Client, Commande, Pharmacien, Pharmacie

from .Serializers import MedicamentSerializer, CategorieSerializer, ClientSerializer, CommandeSerializer, PharmacienSerializer, PharmacieSerializer

# Create your views here.


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

class PharmacienViewSet(viewsets.ModelViewSet):
    queryset = Pharmacien.objects.all()
    serializer_class = PharmacienSerializer

class PharmacieViewSet(viewsets.ModelViewSet):
    queryset = Pharmacie.objects.all()
    serializer_class = PharmacieSerializer




class MedicamentViewSet(viewsets.ModelViewSet):
    queryset=Medicament.objects.all()
    serializer_class = MedicamentSerializer
