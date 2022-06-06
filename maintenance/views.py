from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction
from rest_framework.response import Response

from .serializers import DemandeInterventionSerializer, InterventionSerializer, PieceRechangeSerializer, PlanEntretienSerializer

from .models import DemandeIntervention, Intervention, PieceRechange, PlanEntretien


class DemandeInterventionViewset(viewsets.ModelViewSet):
    queryset = DemandeIntervention.objects.all()
    serializer_class = DemandeInterventionSerializer
    
    def __str__(self):
        return self.name
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def cloturer(self, request, pk):
        demande = self.get_object()
        demande.etat = False
        demande.save()
        
        return Response()
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def annuler(self, request, pk):
        demande = self.get_object()
        demande.etat = True
        demande.save()
        
        return Response()
    
class InterventionViewset(viewsets.ModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
    
    def __str__(self):
        return self.name
    
class PieceRechangeViewset(viewsets.ModelViewSet):
    queryset = PieceRechange.objects.all()
    serializer_class = PieceRechangeSerializer
    
    def __str__(self):
        return self.name
    
class PlanEntretienViewset(viewsets.ModelViewSet):
    queryset = PlanEntretien.objects.all()
    serializer_class = PlanEntretienSerializer
    
    def __str__(self):
        return self.name