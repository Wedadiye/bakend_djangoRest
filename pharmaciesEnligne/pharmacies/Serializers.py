
from rest_framework import serializers

from .models import*

class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

class PharmacienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacien
        fields = '__all__'

class PharmacieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacie
        fields = '__all__'

