from dataclasses import field
from rest_framework import serializers
from .models import DemandeInterventionGarage, InterventionGarage, PieceRechangeGarage, PlanEntretienGarage
from flotte.serializers import VehiculeSerializer


class DemandeInterventionGarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeInterventionGarage
        fields = '__all__'

class InterventionGarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterventionGarage
        fields = '__all__'

class PieceRechangeGarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieceRechangeGarage
        fields = '__all__'

class PlanEntretienGarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEntretienGarage
        fields = '__all__'