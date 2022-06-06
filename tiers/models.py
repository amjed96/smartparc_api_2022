from django.db import models


class Tiers(models.Model):
    
    compte = models.CharField(max_length=25, null=True, blank=True)
    intitule = models.CharField(max_length=25, null=True, blank=True)
    abrege = models.CharField(max_length=25, null=True, blank=True)
    compte_collectif = models.CharField(max_length=25, null=True, blank=True)
    qualite = models.CharField(max_length=25, null=True, blank=True)
    interlocuteur = models.CharField(max_length=25, null=True, blank=True)
    commentaire = models.TextField(max_length=255, null=True, blank=True)
    type = models.BooleanField(null=True, blank=True)
    
class Contact(models.Model):
    
    tiers = models.ForeignKey('tiers.Tiers', null=True, on_delete=models.SET_NULL, related_name='contacts_tiers', blank=True)
    type = models.CharField(max_length=25, null=True, blank=True)
    civilite = models.CharField(max_length=25, null=True, blank=True)
    nom = models.CharField(max_length=25, null=True, blank=True)
    prenom = models.CharField(max_length=25, null=True, blank=True)
    service = models.CharField(max_length=25, null=True, blank=True)
    fonction = models.CharField(max_length=25, null=True, blank=True)
    telephone = models.CharField(max_length=25, null=True, blank=True)
    portable = models.CharField(max_length=25, null=True, blank=True)
    telecopie = models.CharField(max_length=25, null=True, blank=True)
    skype = models.CharField(max_length=25, null=True, blank=True)
    linkedin = models.CharField(max_length=25, null=True, blank=True)
    facebook = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)