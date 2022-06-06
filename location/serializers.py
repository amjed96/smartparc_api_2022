from rest_framework import serializers

from .models import ContratLocation
from flotte.serializers import VehiculeSerializer


class ContratLocationSerializer(serializers.ModelSerializer):
    #vehicule = VehiculeSerializer(read_only=False)
    class Meta:
        model = ContratLocation
        fields = '__all__'