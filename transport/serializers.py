from rest_framework import serializers

from .models import DossierVoyage, FicheTrajet


class DossierVoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DossierVoyage
        fields = '__all__'
        
class DossierVoyageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DossierVoyage
        fields = '__all__'
        depth = 1
        
class FicheTrajetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FicheTrajet
        fields = '__all__'
        
class FicheTrajetGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FicheTrajet
        fields = '__all__'
        depth = 1