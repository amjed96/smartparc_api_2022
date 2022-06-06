from rest_framework import serializers

from .models import Vehicule, Affectation, ContratLocation, ContratAchat, Consommation
from personnel.serializers import UserSerializer
from personnel.models import User


class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'
        
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