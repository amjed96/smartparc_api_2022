from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.hashers import make_password


class User(AbstractUser):
    
    cin = models.IntegerField(null=True, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    telephone = models.IntegerField(null=True, blank=True)
    qualification = models.CharField(max_length=255,null=True, blank=True)
    type_permis = models.CharField(max_length=255,null=True, blank=True)
    username = models.CharField(max_length=25,null=False,unique=True, blank=False)
    password = models.CharField(max_length=255,null=False, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    affecte = models.BooleanField(default=False)
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        User.objects.filter(pk=instance.id).update(password = make_password(instance.password))
        Token.objects.create(user=instance)
        
'''@receiver(post_edit, sender=settings.AUTH_USER_MODEL)'''


# class UserPersonnelManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not username:
#             raise ValueError('Users must have a username')
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username)
        
#         user.set_password(password)
#         user.save()
        
#         return user
    
#     def creat_superuser(self, email, username, password):
#         user = self.create_user(email, username, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
        
#         return user

# class User(AbstractBaseUser,PermissionsMixin):
#     cin = models.IntegerField(null=True, blank=True)
#     date_naissance = models.DateField(null=True, blank=True)
#     telephone = models.IntegerField(null=True, blank=True)
#     qualification = models.CharField(max_length=255,null=True, blank=True)
#     type_permis = models.CharField(max_length=255,null=True, blank=True)
#     username = models.CharField(max_length=25,null=True,unique=True, blank=True)
#     password = models.CharField(max_length=255,null=True, blank=True)
#     email = models.EmailField(max_length=255, null=True, blank=True)
#     affecte = models.BooleanField()
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
    
#     objects = UserPersonnelManager()
    
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS: 'username'
    
#     def get_full_name(self):
#         return self.username
    
#     def get_short_name(self):
#         return self.username
    
#     def __str__(self):
#         return self.username