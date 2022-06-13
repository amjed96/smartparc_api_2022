from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from personnel.views import UserViewset, CustomAuthToken, PermisViewset, PermisGetViewset, PasseportViewset, PasseportGetViewset, VisiteViewset, VisiteGetViewset
from flotte.views import VehiculeViewset, AffectationViewset, ContratLocationFlotteViewset, ContratAchatViewset, ConsommationViewset, AffectationGetViewset
from achatstock.views import DocumentViewset, DemandeAchatViewset, StockViewset
from finance.views import F_DOCENTETEViewset, F_CREGLEMENTViewset, F_REGLECHViewset, F_DOCREGLViewset
from location.views import ContratLocationViewset
from maintenance.views import DemandeInterventionViewset, InterventionViewset, PieceRechangeViewset, PlanEntretienViewset
from tiers.views import TiersViewset, ContactViewset, ContactGetViewset
from transport.views import FicheTrajetViewset, DossierVoyageViewset, DossierVoyageGetViewset, FicheTrajetGetViewset
from garage.views import DemandeInterventionGarageViewset, InterventionGarageViewset, PieceRechangeGarageViewset, PlanEntretienGarageViewset

from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()

# Personnel
router.register(r'personnel', UserViewset, basename='personnel')
router.register(r'permis', PermisViewset, basename='permis')
router.register(r'permis-get', PermisGetViewset, basename='permis')
router.register(r'passeport', PasseportViewset, basename='passeport')
router.register(r'passeport-get', PasseportGetViewset, basename='passeport')
router.register(r'visite', VisiteViewset, basename='visite')
router.register(r'visite-get', VisiteGetViewset, basename='visite')

# Flotte
router.register(r'vehicule', VehiculeViewset, basename='vehicule')
router.register(r'affectation', AffectationViewset, basename='affectation')
router.register(r'affectation-get', AffectationGetViewset, basename='affectation')
router.register(r'contrat-location-flotte', ContratLocationFlotteViewset, basename='contrat-location-flotte')
router.register(r'contrat-achat', ContratAchatViewset, basename='contrat-achat')
router.register(r'consommation', ConsommationViewset, basename='consommation')

# AchatStock
router.register(r'document', DocumentViewset, basename='document')
router.register(r'demande-achat', DemandeAchatViewset, basename='demande-achat')
router.register(r'stock', StockViewset, basename='stock')

# Finance
router.register(r'doc-entete', F_DOCENTETEViewset, basename='doc-entete')
router.register(r'c-reglement', F_CREGLEMENTViewset, basename='c-reglement')
router.register(r'regl-ech', F_REGLECHViewset, basename='regl-ech')
router.register(r'doc-regl', F_DOCREGLViewset, basename='doc-regl')

# Location
router.register(r'contrat-location', ContratLocationViewset, basename='contrat-location')

# Maintenance
router.register(r'demande-intervention', DemandeInterventionViewset, basename='demande-intervention')
router.register(r'intervention', InterventionViewset, basename='intervention')
router.register(r'piece-rechange', PieceRechangeViewset, basename='piece-rechange')
router.register(r'plan-entretien', PlanEntretienViewset, basename='plan-entretien')

# Tiers
router.register(r'tiers', TiersViewset, basename='tiers')
router.register(r'contact', ContactViewset, basename='contact')
router.register(r'contact-get', ContactGetViewset, basename='contact')

# Transport
router.register(r'dossier-voyage', DossierVoyageViewset, basename='dossier-voyage')
router.register(r'dossier-voyage-get', DossierVoyageGetViewset, basename='dossier-voyage')
router.register(r'fiche-trajet', FicheTrajetViewset, basename='fiche-trajet')
router.register(r'fiche-trajet-get', FicheTrajetGetViewset, basename='fiche-trajet')

#Garage
router.register(r'demande-intervention-garage', DemandeInterventionGarageViewset, basename='demande-intervention-garage')
router.register(r'intervention-garage', InterventionGarageViewset, basename='intervention-garage')
router.register(r'piece-rechange-garage', PieceRechangeGarageViewset, basename='piece-rechange-garage')
router.register(r'plan-entretien-garage', PlanEntretienGarageViewset, basename='plan-entretien-garage')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    
    # path('login/', obtain_auth_token, name='login'),
    path('login/', CustomAuthToken.as_view()),
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/personnel/', include('personnel.urls')),
    
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
