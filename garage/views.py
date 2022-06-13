from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction
from rest_framework.response import Response

from garage.models import DemandeInterventionGarage, InterventionGarage, PieceRechangeGarage, PlanEntretienGarage
from .serializers import DemandeInterventionGarageSerializer, InterventionGarageSerializer, PieceRechangeGarageSerializer, PlanEntretienGarageSerializer


class DemandeInterventionGarageViewset(viewsets.ModelViewSet):
    queryset = DemandeInterventionGarage.objects.all()
    serializer_class = DemandeInterventionGarageSerializer

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

class InterventionGarageViewset(viewsets.ModelViewSet):
    queryset = InterventionGarage.objects.all()
    serializer_class = InterventionGarageSerializer
    
    def __str__(self):
        return self.name

class PieceRechangeGarageViewset(viewsets.ModelViewSet):
    queryset = PieceRechangeGarage.objects.all()
    serializer_class = PieceRechangeGarageSerializer
    
    def __str__(self):
        return self.name
    
class PlanEntretienGarageViewset(viewsets.ModelViewSet):
    queryset = PlanEntretienGarage.objects.all()
    serializer_class = PlanEntretienGarageSerializer
    
    def __str__(self):
        return self.name