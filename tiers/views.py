from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactGetSerializer, TiersSerializer, ContactSerializer

from .models import Tiers, Contact


class TiersViewset(viewsets.ModelViewSet):
    queryset = Tiers.objects.all()
    serializer_class = TiersSerializer
    
    # def get_queryset(self):
        
    #     queryset = Tiers.objects.all()
        
    #     type = self.request.GET.get('type')
        
    #     if type is not None:
    #         queryset = queryset.filter(type = type)
        
    #     return queryset
    
class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class ContactGetViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactGetSerializer