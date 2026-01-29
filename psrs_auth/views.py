from django.shortcuts import render
from .serializers import CustomTokenObtainPairSerializer, RegisterSerializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model



User = get_user_model()


# Create your views here.
class EmailTokenObtainedView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = RegisterSerializers