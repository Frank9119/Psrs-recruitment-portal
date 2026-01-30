from django.urls import path
from . import views
from .views import RegisterView,ResetPasswordView


# URL Configurations
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('reset-password/', ResetPasswordView.as_view(), name="reset password"),
    
]
