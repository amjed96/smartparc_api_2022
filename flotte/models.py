from django.db import models


class Vehicule(models.Model):
    
    immatriculation = models.CharField(max_length=25, primary_key=True)
    num_serie = models.CharField(max_length=25, blank=True, null=True)
    kilometrage = models.IntegerField(blank=True, null=True)
    engin = models.CharField(max_length=25, blank=True, null=True)
    consommation = models.CharField(max_length=25, blank=True, null=True)
    entretien = models.CharField(max_length=25, blank=True, null=True)
    constructeur = models.CharField(max_length=25, blank=True, null=True)
    type_commercial = models.CharField(max_length=25, blank=True, null=True)
    activite = models.CharField(max_length=25, blank=True, null=True)
    genre = models.CharField(max_length=25, blank=True, null=True)
    type_constructeur = models.CharField(max_length=25, blank=True, null=True)
    date_pmc = models.DateField(blank=True, null=True)
    carrosserie = models.CharField(max_length=25, blank=True, null=True)
    energie = models.CharField(max_length=25, blank=True, null=True)
    puissance_fiscale = models.IntegerField(blank=True, null=True)
    nombre_essieux = models.IntegerField(blank=True, null=True)
    charge_utile = models.IntegerField(blank=True, null=True)
    poids_vide = models.IntegerField(blank=True, null=True)
    ptac_ptra = models.IntegerField(blank=True, null=True)
    nombre_places = models.IntegerField(blank=True, null=True)
    nombre_debout = models.IntegerField(blank=True, null=True)
    cylidree = models.IntegerField(blank=True, null=True)
    a_louer = models.BooleanField(default=False,blank=True)
    affecte = models.BooleanField(default=False,blank=True)
    
class Affectation(models.Model):
    
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='vehicule_affectation', blank=True)
    # vehicule = models.OneToOneField('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='vehicule_affectation', blank=True)
    chauffeur = models.ForeignKey('personnel.User', null=True, on_delete=models.SET_NULL, related_name='chauffeur_affectation', blank=True)
    # chauffeur = models.OneToOneField('personnel.User', null=True, on_delete=models.SET_NULL, related_name='chauffeur_affectation', blank=True)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    etat = models.BooleanField(default=True, blank=True)
    
class Consommation(models.Model):
    
    mois = models.DateField(blank=True, null=True)
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='vehicule_consommation', blank=True)
    type = models.CharField(max_length=25, blank=True, null=True)
    kilometrage = models.IntegerField(blank=True, null=True)
    consommation_totale = models.IntegerField(blank=True, null=True)
    consommation = models.IntegerField(blank=True, null=True)
    
class ContratAchat(models.Model):
    
    date = models.DateField()
    vendeur = models.CharField(max_length=25, blank=True, null=True)
    # vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='vehicule_contrat_achat', blank=True)
    vehicule = models.OneToOneField('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='vehicule_contrat_achat', blank=True)
    marque = models.CharField(max_length=25, blank=True, null=True)
    modele = models.CharField(max_length=25, blank=True, null=True)
    chassis = models.CharField(max_length=25, blank=True, null=True)
    moteur = models.CharField(max_length=25, blank=True, null=True)
    prix = models.IntegerField(blank=True, null=True)
    
class ContratLocation(models.Model):
    
    # vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='vehicule_contrat_location', blank=True)
    vehicule = models.OneToOneField('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='vehicule_contrat_location', blank=True)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    marque = models.CharField(max_length=25, blank=True, null=True)
    modele = models.CharField(max_length=25, blank=True, null=True)
    prix = models.IntegerField(blank=True, null=True)