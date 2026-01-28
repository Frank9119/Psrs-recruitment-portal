from django.db import models
from django.contrib.auth.models import AbstractUser  # (django.contrib.auth.models)
from django.conf import settings
from psrs_mixin.models import BaseModel 



USER_ROLES = (
    ('ADMIN', 'Admin'),
    ('APPLICANT', 'Applicant'),
    ('RECRUITER', 'Recruiter'),

)



# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='APPLICANT')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['email']


class UserProfile(BaseModel):
    """
    Profile model that extends the user model. Including applicant points
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    class Meta:
        verbose_name = 'User_profile'
        verbose_name_plural = 'User_profiles'
        ordering = ['-primary_key']


