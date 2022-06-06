from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from personnel.views import UserViewset, CustomAuthToken

from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()

# Personnel
router.register(r'personnel', UserViewset, basename='personnel')

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
