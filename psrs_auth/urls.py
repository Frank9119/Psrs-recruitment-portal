from django.urls import path
from . import views
from .views import RegisterView


# URL Configurations
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    
]
