from rest_framework import serializers

from .models import Tiers, Contact


class TiersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiers
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
class ContactGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        depth = 1