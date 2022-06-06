from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction
from rest_framework.response import Response

from .serializers import AffectationGetSerializer, VehiculeSerializer, AffectationSerializer, ContratLocationSerializer, ContratAchatSerializer, ConsommationSerializer

from .models import Vehicule, Affectation, ContratLocation, ContratAchat, Consommation

# Create your views here.


class VehiculeViewset(viewsets.ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer
    
    def __str__(self):
        return self.name
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def affecter(self, request, pk):
        vehicule = self.get_object()
        vehicule.affecte = True
        vehicule.save()
        
        return Response()
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def desaffecter(self, request, pk):
        vehicule = self.get_object()
        vehicule.affecte = False
        vehicule.save()
        
        return Response()
    
class AffectationViewset(viewsets.ModelViewSet):
    queryset = Affectation.objects.all()
    serializer_class = AffectationSerializer
    
    def __str__(self):
        return self.name
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def cloturer(self, request, pk):
        affectation = self.get_object()
        affectation.etat = False
        affectation.save()
        
        return Response()
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def annuler(self, request, pk):
        affectation = self.get_object()
        affectation.etat = True
        affectation.save()
        
        return Response()
    
class AffectationGetViewset(viewsets.ModelViewSet):
    queryset = Affectation.objects.all()
    serializer_class = AffectationGetSerializer
    
    def __str__(self):
        return self.name
    
class ContratLocationFlotteViewset(viewsets.ModelViewSet):
    queryset = ContratLocation.objects.all()
    serializer_class = ContratLocationSerializer
    
    def __str__(self):
        return self.name
    
class ContratAchatViewset(viewsets.ModelViewSet):
    #queryset = ContratAchat.objects.all()
    serializer_class = ContratAchatSerializer
    
    def get_queryset(self):
    # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = ContratAchat.objects.all()
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        vehicule = self.request.GET.get('vehicule')
        if vehicule is not None:
            queryset = queryset.filter(vehicule=vehicule)
        return queryset
    
    def __str__(self):
        return self.name
    
class ConsommationViewset(viewsets.ModelViewSet):
    queryset = Consommation.objects.all()
    serializer_class = ConsommationSerializer
    
    def __str__(self):
        return self.name