from rest_framework import serializers

from .models import F_DOCENTETE, F_CREGLEMENT, F_REGLECH, F_DOCREGL


class F_DOCENTETESerializer(serializers.ModelSerializer):
    class Meta:
        model = F_DOCENTETE
        fields = '__all__'
        
class F_CREGLEMENTSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_CREGLEMENT
        fields = '__all__'
        
class F_REGLECHSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_REGLECH
        fields = '__all__'
        
class F_DOCREGLSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_DOCREGL
        fields = '__all__'