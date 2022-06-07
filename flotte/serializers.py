from rest_framework import serializers

from .models import Vehicule, Affectation, ContratLocation, ContratAchat, Consommation
from personnel.serializers import UserSerializer
from personnel.models import User


class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = [
            'immatriculation',
            'num_serie',
            'kilometrage',
            'engin',
            'consommation',
            'entretien',
            'constructeur',
            'type_commercial',
            'activite',
            'genre',
            'type_constructeur',
            'date_pmc',
            'carrosserie',
            'energie',
            'puissance_fiscale',
            'nombre_essieux',
            'charge_utile',
            'poids_vide',
            'ptac_ptra',
            'nombre_places',
            'nombre_debout',
            'cylidree',
            'a_louer',
            'affecte',
            'vehicule_contrat_achat',
            'vehicule_contrat_location',
        ]
        # vehicule_contrat_achat
        
class AffectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affectation
        fields = '__all__'
    
class AffectationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affectation
        fields = '__all__'
        depth=1
        
class ContratLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratLocation
        fields = '__all__'
        
class ContratAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratAchat
        fields = '__all__'
        
class ConsommationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consommation
        fields = '__all__'