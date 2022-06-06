from django.shortcuts import render
from rest_framework import viewsets
from .serializers import F_DOCENTETESerializer, F_CREGLEMENTSerializer, F_REGLECHSerializer, F_DOCREGLSerializer

from  .models import F_DOCENTETE, F_CREGLEMENT, F_REGLECH, F_DOCREGL


class F_DOCENTETEViewset(viewsets.ModelViewSet):
    queryset = F_DOCENTETE.objects.all()
    serializer_class = F_DOCENTETESerializer
    
    def __str__(self):
        return self.name
    
class F_CREGLEMENTViewset(viewsets.ModelViewSet):
    queryset = F_CREGLEMENT.objects.all()
    serializer_class = F_CREGLEMENTSerializer
    
    def __str__(self):
        return self.name
    
class F_REGLECHViewset(viewsets.ModelViewSet):
    queryset = F_REGLECH.objects.all()
    serializer_class = F_REGLECHSerializer
    
    def __str__(self):
        return self.name
    
class F_DOCREGLViewset(viewsets.ModelViewSet):
    queryset = F_DOCREGL.objects.all()
    serializer_class = F_DOCREGLSerializer
    
    def __str__(self):
        return self.name
