from django.db import models


class DemandeInterventionGarage(models.Model):
    
    date_demande = models.DateField(null=True, blank=True)
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='demande_vehicule_garage', blank=True)
    type = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    etat = models.BooleanField(null=True, blank=True)
    
class InterventionGarage(models.Model):
    
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='intervention_vehicule_garage', blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    objet = models.CharField(max_length=25, null=True, blank=True)
    entreprise = models.CharField(max_length=25, null=True, blank=True)
    montant_mo_ht = models.IntegerField(null=True, blank=True)
    montant_pieces_ht = models.IntegerField(null=True, blank=True)
    montant_total_ht = models.IntegerField(null=True, blank=True)
    collaborateur = models.CharField(max_length=25, null=True, blank=True)
    
class PieceRechangeGarage(models.Model):
    
    code = models.CharField(max_length=25, primary_key=True)
    nom = models.CharField(max_length=25, null=True, blank=True)
    code_casier = models.CharField(max_length=25, null=True, blank=True)
    famille = models.CharField(max_length=25, null=True, blank=True)
    categorie = models.CharField(max_length=25, null=True, blank=True)
    unite = models.CharField(max_length=25, null=True, blank=True)
    prix = models.IntegerField(null=True, blank=True)
    nombre = models.IntegerField(null=True, blank=True)
    # ManyToOne avec Vehicule 0..0
    
class PlanEntretienGarage(models.Model):
    
    operation = models.CharField(max_length=25, null=True, blank=True)
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='plan_vehicule_garage', blank=True)
    type = models.CharField(max_length=25, null=True, blank=True)
    frequence = models.IntegerField(null=True, blank=True)
    unite = models.CharField(max_length=25, null=True, blank=True)