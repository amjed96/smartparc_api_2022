from django.db import models

class Document(models.Model):
    
    type = models.CharField(max_length=25, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    numero = models.CharField(max_length=25, null=True, blank=True)
    tiers = models.ForeignKey('tiers.Tiers', null=True, on_delete=models.SET_NULL, related_name='documents_tiers', blank=True)
    
class DemandeAchat(models.Model):
    
    date = models.DateField(null=True, blank=True)
    demandeur = models.ForeignKey('personnel.User', null=True, on_delete=models.SET_NULL, related_name='personnel_demande_achat', blank=True)
    article = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    statut = models.BooleanField(null=True, blank=True)
    
class Stock(models.Model):
    
    reference = models.CharField(max_length=25, primary_key=True)
    article = models.CharField(max_length=25, null=True, blank=True)
    codecasier = models.CharField(max_length=25, null=True, blank=True)
    dateachat = models.DateField(null=True, blank=True)
    quantite = models.IntegerField(null=True, blank=True)
    unite = models.CharField(max_length=25, null=True, blank=True)