from django.shortcuts import render
from .serializers import CustomTokenObtainPairSerializer, RegisterSerializers, PasswordResetSerializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model

## for reset password view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



User = get_user_model()


# Create your views here.
class EmailTokenObtainedView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = RegisterSerializers



class ResetPasswordView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # validate data
        email = serializer.validated_data['email']
        new_password = serializer.validated_data['new_password']

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()

        except User.DoesNotExist:
            return Response({'error': "User Not Found"}, status=404)


## Adding login page
def index(request):
    return render(request,'../psrs_templates/loginPage.html',{'name':"Login or Signup"})