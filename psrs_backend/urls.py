from django.contrib import admin
from django.urls import path, include

# Rest Framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from psrs_auth.views import EmailTokenObtainedView









# URL Configurations
urlpatterns = [
    path('admin/', admin.site.urls),
    path('psrs/', include('psrs_job.urls')),
    # authentication
    path('auth/', include('psrs_auth.urls')),
    path('auth/login/', EmailTokenObtainedView.as_view(), name="token_obtained_pair"),
    path('api/token/refresh', TokenRefreshView.as_view(), name="refresh_token" ),
    # path('api/token/', TokenObtainPairView.as_view(), name="token_obtained_pair"),


    
]
