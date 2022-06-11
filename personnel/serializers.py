from asyncio.windows_events import NULL
from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

from django.contrib.auth.hashers import make_password

from .models import User, Permis, Passeport, Visite


class UserSerializer(serializers.ModelSerializer): ##### TO DO #####
    class Meta:
        User = get_user_model()
        model = User
        fields = [
            "id",
            "last_login",
            "is_superuser",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
            "cin",
            "date_naissance",
            "telephone",
            "qualification",
            "type_permis",
            "username",
            "password",
            "email",
            "affecte",
            "groups",
            "user_permissions",
            "permis_personnel",
            "passeport_personnel",
            "visites_personnel",
        ]
        
    # def create(self, validated_data):
    #     '''user = User.objects.create(
    #         is_superuser = validated_data['is_superuser'],
    #         first_name = validated_data['first_name'],
    #         last_name = validated_data['last_name'],
    #         email = validated_data['email'],
    #         is_staff = True,
    #         is_active = True,
    #         cin = validated_data['cin'],
    #         date_naissance = validated_data['date_naissance'],
    #         telephone = validated_data['telephone'],
    #         qualification = validated_data['qualification'],
    #         type_permis = validated_data['type_permis'],
    #         username = validated_data['username'],
    #         password = make_password(validated_data['password']),
    #         affecte = validated_data['affecte']
    #     )'''
    #     user = User()
        
    #     user.is_superuser = validated_data['is_superuser']
    #     user.first_name = validated_data['first_name']
    #     user.last_name = validated_data['last_name']   
    #     user.email = validated_data['email']
    #     user.is_staff = validated_data['is_staff']
    #     user.is_active = validated_data['is_active']
    #     user.cin = validated_data['cin']
    #     user.date_naissance = validated_data['date_naissance']
    #     user.telephone = validated_data['telephone']
    #     user.qualification = validated_data['qualification']
    #     user.type_permis = validated_data['type_permis']
    #     user.username = validated_data['username']
    #     user.password = make_password(validated_data['password'])
    #     user.affecte = validated_data['affecte']
        
    #     user.save()
                
    #     return user
    
    def update(self, instance, validated_data):
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.cin = validated_data.get('cin', instance.cin)
        instance.date_naissance = validated_data.get('date_naissance', instance.date_naissance)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.qualification = validated_data.get('qualification', instance.qualification)
        instance.type_permis = validated_data.get('type_permis', instance.type_permis)
        instance.username = validated_data.get('username', instance.username)
        instance.password = make_password(validated_data.get('password', instance.password))
        instance.affecte = validated_data.get('affecte', instance.affecte)
        
        instance.save()
        return instance

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "last_login",
            "is_superuser",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
            "cin",
            "date_naissance",
            "telephone",
            "qualification",
            "type_permis",
            "username",
            "password",
            "email",
            "affecte",
            "groups",
            "user_permissions",
            "permis_personnel",
            "passeport_personnel",
            "visites_personnel",
        ]
        depth = 1
    
class PermisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permis
        fields = '__all__'
        
class PermisGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permis
        fields = '__all__'
        depth = 1
        
class PasseportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passeport
        fields = '__all__'
        
class PasseportGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passeport
        fields = '__all__'
        depth = 1
        
class VisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visite
        fields = '__all__'
        
class VisiteGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visite
        fields = '__all__'
        depth = 1