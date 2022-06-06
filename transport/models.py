from django.db import models


class DossierVoyage(models.Model):
    
    code = models.CharField(max_length=25, primary_key=True)    
    numero = models.IntegerField(null=True, blank=True)
    ref_aller = models.IntegerField(null=True, blank=True)
    date_creation = models.DateField(null=True, blank=True)
    chauffeur = models.ForeignKey('personnel.User', null=True, on_delete=models.SET_NULL, related_name='dossiers_voyage_personnel', blank=True)
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='dossiers_voyage_vehicule', blank=True)
    remorque = models.CharField(max_length=25, null=True, blank=True)
    client = models.ForeignKey('tiers.Tiers', null=True, on_delete=models.SET_NULL, related_name='dossiers_voyage_client', blank=True)
    voyage = models.CharField(max_length=25, null=True, blank=True)
    date_chargement = models.DateField(null=True, blank=True)
    date_dechargement = models.DateField(null=True, blank=True)
    montant_ht = models.IntegerField(null=True, blank=True)
    etat = models.BooleanField(null=True, blank=True)
    
class FicheTrajet(models.Model):
    
    nom = models.CharField(max_length=25, null=True, blank=True)
    client = models.ForeignKey('tiers.Tiers', null=True, on_delete=models.SET_NULL, related_name='fiche_trajet_tiers', blank=True)
    marchandise = models.CharField(max_length=25, null=True, blank=True)
    trajet = models.CharField(max_length=25, null=True, blank=True)
    unite = models.CharField(max_length=25, null=True, blank=True)
    type_prestation = models.CharField(max_length=25, null=True, blank=True)
    categorie = models.CharField(max_length=25, null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    prix = models.IntegerField(null=True, blank=True)
    prix_retour = models.IntegerField(null=True, blank=True)