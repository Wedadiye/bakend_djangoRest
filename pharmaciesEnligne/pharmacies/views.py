from http.client import responses
from pstats import Stats, StatsProfile
import statistics
from django.shortcuts import render
from rest_framework.decorators import action 
from rest_framework.response import Response as response
# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ViewSet

from rest_framework import status ,viewsets

from .models import Medicament, Categorie, Client, Commande, Pharmacien, Pharmacie
from django.contrib.auth.models import User

from .Serializers import MedicamentSerializer, CategorieSerializer, ClientSerializer, CommandeSerializer, PharmacienSerializer, PharmacieSerializer
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authtoken.models import Token

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
       
    
    def list(self, request):
        username = request.query_params.get('username')
        password = request.query_params.get('password')

        if username is None or password is None:
            # Si les paramètres d'authentification ne sont pas fournis, renvoyer la liste de tous les pharmaciens
            pharmaciens = self.queryset
        else:
            # Vérifier l'authentification en filtrant les pharmaciens par nom d'utilisateur et mot de passe
            pharmaciens = Pharmacien.objects.filter(username=username, password=password)

        serializer = self.serializer_class(pharmaciens, many=True)
        return Response(serializer.data)
    
class PharmacieViewSet(viewsets.ModelViewSet):
    queryset = Pharmacie.objects.all()
    serializer_class = PharmacieSerializer

class MedicamentViewSet(viewsets.ModelViewSet):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
    

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
        try:
            medicament = self.get_queryset().get(pk=pk)
            medicament.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Medicament.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
   
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data)
    
   
    #pour lister tous les medicament d 'un pharmacien 
    def get_queryset(self):
        pharmacien_id = self.request.query_params.get('pharmacien_id')
        if pharmacien_id:
            return self.queryset.filter(pharmacie__Pharmacien__id=pharmacien_id)
        
        return self.queryset



    # Méthode pour mettre à jour un médicament
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
class MedicamentPharmacieViewSet(viewsets.ModelViewSet):
    queryset=Medicament.objects.all()
    serializer_class = MedicamentSerializer
    
    @action(detail=True, methods=['GET'])
    def by_pharmacie(self, request, pk=None):
        try:
            pharmacie = Pharmacie.objects.get(pk=pk)
            medicaments = Medicament.objects.filter(pharmacie=pharmacie)
            serializer = MedicamentSerializer(medicaments, many=True)
            return response(serializer.data)
        except Pharmacie.DoesNotExist:
            return response({'error': 'Pharmacie non trouvée'}, status=status.HTTP_404_NOT_FOUND)


    
class MedicamentPharmaciePharmacienViewSet(viewsets.ViewSet):
    def list(self, request, pharmacien_id=None):
        pharmacies = Pharmacie.objects.filter(Pharmacien_id=pharmacien_id)
        pharmacies_data = PharmacieSerializer(pharmacies, many=True).data
        response_data = []

        for pharmacy in pharmacies:
            medicaments = Medicament.objects.filter(pharmacie=pharmacy)
            medicaments_data = MedicamentSerializer(medicaments, many=True).data
            response_data.append({
                'pharmacie': PharmacieSerializer(pharmacy).data,
                'medicaments': medicaments_data
            })

        return Response(response_data)


        
    
class PharmacieMedicamentsViewSet(viewsets.ViewSet):
    def list(self, request, pharmacien_id=None):
        pharmacies = Pharmacie.objects.filter(Pharmacien_id=pharmacien_id)
        serializer = PharmacieSerializer(pharmacies, many=True)

        response_data = []
        for pharmacy_data in serializer.data:
            pharmacy_id = pharmacy_data['id']
            medicaments = Medicament.objects.filter(pharmacie_id=pharmacy_id)
            medicament_serializer = MedicamentSerializer(medicaments, many=True)
            response_data.append({
                'pharmacie': pharmacy_data,
                'medicaments': medicament_serializer.data
            })

        return Response(response_data)