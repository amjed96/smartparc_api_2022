from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction
from rest_framework.response import Response

from .serializers import DossierVoyageSerializer, FicheTrajetSerializer, DossierVoyageGetSerializer, FicheTrajetGetSerializer

from  .models import DossierVoyage, FicheTrajet


class DossierVoyageViewset(viewsets.ModelViewSet):
    queryset = DossierVoyage.objects.all()
    serializer_class = DossierVoyageSerializer
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def cloturer(self, request, pk):
        dossier = self.get_object()
        dossier.etat = False
        dossier.save()
        
        return Response()
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def annuler(self, request, pk):
        dossier = self.get_object()
        dossier.etat = True
        dossier.save()
        
        return Response()
    
class DossierVoyageGetViewset(viewsets.ModelViewSet):
    queryset = DossierVoyage.objects.all()
    serializer_class = DossierVoyageGetSerializer
    
class FicheTrajetViewset(viewsets.ModelViewSet):
    queryset = FicheTrajet.objects.all()
    serializer_class = FicheTrajetSerializer
    
class FicheTrajetGetViewset(viewsets.ModelViewSet):
    queryset = FicheTrajet.objects.all()
    serializer_class = FicheTrajetGetSerializer