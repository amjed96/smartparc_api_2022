from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction
from rest_framework.response import Response

from .serializers import DocumentSerializer, DemandeAchatSerializer, StockSerializer

from  .models import Document, DemandeAchat, Stock


class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    def __str__(self):
        return self.name
    
class DemandeAchatViewset(viewsets.ModelViewSet):
    queryset = DemandeAchat.objects.all()
    serializer_class = DemandeAchatSerializer
    
    def __str__(self):
        return self.name
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def cloturer(self, request, pk):
        demande = self.get_object()
        demande.statut = False
        demande.save()
        
        return Response()
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def annuler(self, request, pk):
        demande = self.get_object()
        demande.statut = True
        demande.save()
        
        return Response()
    
class StockViewset(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
    def __str__(self):
        return self.name