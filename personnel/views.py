from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction

from .models import User
from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class UserViewset(viewsets.ModelViewSet): ##### TO DO #####
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        
        queryset = User.objects.all()
        
        qualification = self.request.GET.get('qualification')
        
        if qualification is not None:
            queryset = queryset.filter(qualification = qualification)
        
        return queryset
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def affecter(self, request, pk):
        chauffeur = self.get_object()
        chauffeur.affecte = True
        chauffeur.save()
        
        return Response()
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def desaffecter(self, request, pk):
        chauffeur = self.get_object()
        chauffeur.affecte = False
        chauffeur.save()
        
        return Response()
    
    @action(detail=False, methods=['get'])
    def get_loggedin(self, request):
        if request.user.is_anonymous == False:
            return Response(UserSerializer(request.user).data)
        return Response('No user loggedin')
            
    def __str__(self):
        return self.name
    
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_return = User.objects.get(pk=user.pk)
        return Response({
            'token': token.key,
            'user': {
                'id': user.pk,
                'is_superuser': user.is_superuser,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'cin': user.cin,
                'date_naissance': user.date_naissance,
                'telephone': user.telephone,
                'qualification': user.qualification,
                'type_permis': user.type_permis,
                'username': user.username,
                # 'user_password': user.password,
                'affecte': user.affecte,
            }
            # 'user_id': user.pk,
            # 'user_is_superuser': user.is_superuser,
            # 'user_first_name': user.first_name,
            # 'user_last_name': user.last_name,
            # 'user_email': user.email,
            # 'user_is_staff': user.is_staff,
            # 'user_is_active': user.is_active,
            # 'user_cin': user.cin,
            # 'user_date_naissance': user.date_naissance,
            # 'user_telephone': user.telephone,
            # 'user_qualification': user.qualification,
            # 'user_type_permis': user.type_permis,
            # 'user_username': user.username,
            # # 'user_password': user.password,
            # 'user_affecte': user.affecte,
        })

# class SignupView(APIView):
#     permission_classes = (permissions.AllowAny, )
    
#     def post(self, request, format=None):
#         data = self.request.data
        
#         username = data['username']
#         email = data['email']
#         password = data['password']
#         password2 = data['password2']
        
#         if password == password2:
#             if User.objects.filter(username=username).exists():
#                 return Response({'error': 'Username already exists'})
#             else:
#                 user = User.objects.create_user(email=email,password=password,username=username)
                
#                 user.save()
#                 return Response({'success': 'User created successfully'})
#         else:
#             return Response({'error': 'Passwords do not match'})