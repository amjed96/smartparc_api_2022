from django.db import models


class ContratLocation(models.Model):
    
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='vehicule_location', blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    marque = models.CharField(max_length=25, null=True, blank=True)
    modele = models.CharField(max_length=25, null=True, blank=True)
    prix = models.IntegerField(null=True, blank=True)