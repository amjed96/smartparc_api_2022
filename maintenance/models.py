from django.db import models


class DemandeIntervention(models.Model):
    
    date_demande = models.DateField(null=True)
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='demande_vehicule')
    type = models.CharField(max_length=25, null=True)
    description = models.TextField(max_length=255, null=True)
    etat = models.BooleanField(null=True)
    
class Intervention(models.Model):
    
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='intervention_vehicule')
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    objet = models.CharField(max_length=25, null=True)
    entreprise = models.CharField(max_length=25, null=True)
    montant_mo_ht = models.IntegerField(null=True)
    montant_pieces_ht = models.IntegerField(null=True)
    montant_total_ht = models.IntegerField(null=True)
    collaborateur = models.CharField(max_length=25, null=True)
    
class PieceRechange(models.Model):
    
    code = models.CharField(max_length=25, primary_key=True)
    nom = models.CharField(max_length=25, null=True)
    code_casier = models.CharField(max_length=25, null=True)
    famille = models.CharField(max_length=25, null=True)
    categorie = models.CharField(max_length=25, null=True)
    unite = models.CharField(max_length=25, null=True)
    prix = models.IntegerField(null=True)
    nombre = models.IntegerField(null=True)
    # ManyToOne avec Vehicule 0..0
    
class PlanEntretien(models.Model):
    
    operation = models.CharField(max_length=25, null=True)
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='plan_vehicule')
    type = models.CharField(max_length=25, null=True)
    frequence = models.IntegerField(null=True)
    unite = models.CharField(max_length=25, null=True)