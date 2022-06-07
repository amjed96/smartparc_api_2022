from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction
from rest_framework.response import Response

from .serializers import AffectationGetSerializer, VehiculeSerializer, AffectationSerializer, ContratLocationSerializer, ContratAchatSerializer, ConsommationSerializer

from .models import Vehicule, Affectation, ContratLocation, ContratAchat, Consommation
from personnel.models import User


class VehiculeViewset(viewsets.ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer

    # def get_queryset(self):
    #     queryset = Vehicule.objects.all()

    #     contrat_location = self.request.GET.get('vehicule_contrat_location')
    #     contrat_vente = self.request.GET.get('vehicule_contrat_achat')

    #     if contrat_location or contrat_vente is not None:
    #         queryset = queryset.filter(contrat_location)

    @action(detail=False, methods=['get'])
    def get_uncontracted(self, request):
        queryset = Vehicule.objects.filter(vehicule_contrat_achat__isnull = True, vehicule_contrat_location__isnull = True)

        return Response(VehiculeSerializer(queryset, many=True).data)

    @action(detail=False, methods=['get'])
    def get_unaffected(self, request):
        queryset = Vehicule.objects.filter(affecte = False)

        return Response(VehiculeSerializer(queryset, many=True).data)


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

    def create(self, request, *args, **kwargs):
        
        affectation_data = request.data

        #vehicule = Vehicule.objects.get(pk=affectation.vehicule)
        # print(vehicule.immatriculation)

        new_affectation = Affectation.objects.create(
            vehicule = Vehicule.objects.get(pk=affectation_data['vehicule']),
            chauffeur = User.objects.get(pk=affectation_data['chauffeur']),
            date_debut = affectation_data['date_debut'],
            date_fin = affectation_data['date_fin'],
            # etat = affectation_data['etat'],
        )

        # print(new_affectation.vehicule.immatriculation)
        
        vehicule = Vehicule.objects.get(pk=new_affectation.vehicule.immatriculation)
        print(vehicule.immatriculation)
        vehicule.affecte = True
        vehicule.save()

        chauffeur = User.objects.get(pk=new_affectation.chauffeur.id)
        print(chauffeur.username)
        chauffeur.affecte = True
        chauffeur.save()

        new_affectation.save()
        
        # return super().create(request, *args, **kwargs)

        serializer = AffectationSerializer(new_affectation)

        return Response(serializer.data)
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def cloturer(self, request, pk):
        affectation = self.get_object()
        affectation.etat = False
        
        # Désaffecter véhicule
        vehicule = Vehicule.objects.get(pk=affectation.vehicule.immatriculation)
        vehicule.affecte = False
        vehicule.save()

        # Désaffecter chauffeur
        chauffeur = User.objects.get(pk=affectation.chauffeur.id)
        chauffeur.affecte = False
        chauffeur.save()

        affectation.save()
        
        return Response()
    
    #### ICI ###

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